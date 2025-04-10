## IMPORT MODULES
import cv2
import numpy as np
 
## LOAD IMAGE
image_path = "images/3.jpg"
image_original = cv2.imread(image_path)

## RESIZE IMAGE
image = cv2.resize(image_original, (320, 320))
 
## CREATE COPIES FOR DIFFERENT MODELS
## ANNOTATED IMAGE
annotated_image = image.copy()  # For all models
annotated_db50_image = image.copy()  # For DB50
annotated_db18_image = image.copy()  # For DB18
annotated_east_image = image.copy()  # For EAST

## ORIGINAL IMAGE
orig_image = image.copy()  # For inpainting (all models)
orig_db50_image = image.copy()  # For DB50
orig_db18_image = image.copy()  # For DB18
orig_east_image = image.copy()  # For EAST

## SET INPUT IMAGE SIZE
inputSize = (320, 320)
 
## LOAD PRE-TRAINED MODELS
textDetectorEAST = cv2.dnn_TextDetectionModel_EAST("models/frozen_east_text_detection.pb")
textDetectorDB50 = cv2.dnn_TextDetectionModel_DB("models/DB_TD500_resnet50.onnx")
textDetectorDB18 = cv2.dnn_TextDetectionModel_DB("models/DB_TD500_resnet18.onnx")
 
## DECLARE VARIABLES/PARAMETERS FOR THE MODELS
conf_thresh = 0.8
nms_thresh = 0.4
bin_thresh = 0.3
poly_thresh = 0.5
mean = (122.67891434, 116.66876762, 104.00698793)

## SET VARIABLES/PARAMETERS FOR THE MODELS
textDetectorEAST.setConfidenceThreshold(conf_thresh).setNMSThreshold(nms_thresh)
textDetectorEAST.setInputParams(1.0, inputSize, (123.68, 116.78, 103.94), True)

textDetectorDB18.setBinaryThreshold(bin_thresh).setPolygonThreshold(poly_thresh)
textDetectorDB18.setInputParams(1.0/255, inputSize, mean, True)

textDetectorDB50.setBinaryThreshold(bin_thresh).setPolygonThreshold(poly_thresh)
textDetectorDB50.setInputParams(1.0/255, inputSize, mean, True)
 
## CREATE INPAINTING MASKS
inpaint_mask = np.zeros(image.shape[:2], dtype=np.uint8)  # Mask for all models
inpaint_mask_db50 = np.zeros(image.shape[:2], dtype=np.uint8)  # Mask for DB50 only
inpaint_mask_db18 = np.zeros(image.shape[:2], dtype=np.uint8)  # Mask for DB18 only
inpaint_mask_east = np.zeros(image.shape[:2], dtype=np.uint8)  # Mask for EAST only
 
## DETECT TEXT USING MODELS
boxesEAST, _ = textDetectorEAST.detect(image)
boxesDB18, _ = textDetectorDB18.detect(image)
boxesDB50, _ = textDetectorDB50.detect(image)
 
## PROCESS ALL DETECTED BOXES
for box in boxesEAST + boxesDB18 + boxesDB50:
    cv2.fillPoly(inpaint_mask, [np.array(box, np.int32)], 255)  # Full mask
    cv2.polylines(annotated_image, [np.array(box, np.int32)], isClosed=True, color=(0, 255, 0), thickness=1)  # Annotate all models (Green)
 
 ## PROCESS DETECTED BOXES IN DB50
for box in boxesDB50:
    cv2.fillPoly(inpaint_mask_db50, [np.array(box, np.int32)], 255)  # DB50 mask
    cv2.polylines(annotated_db50_image, [np.array(box, np.int32)], isClosed=True, color=(0, 0, 255), thickness=1)  # Annotate DB50 (Red)
 
## PROCESS DETECTED BOXES IN DB18
for box in boxesDB18:
    cv2.fillPoly(inpaint_mask_db18, [np.array(box, np.int32)], 255)  # DB18 mask
    cv2.polylines(annotated_db18_image, [np.array(box, np.int32)], isClosed=True, color=(255, 0, 0), thickness=1)  # Annotate DB18 (Blue)
 
## PROCESS DETECTED BOXES IN EAST
for box in boxesEAST:
    cv2.fillPoly(inpaint_mask_east, [np.array(box, np.int32)], 255)  # EAST mask
    cv2.polylines(annotated_east_image, [np.array(box, np.int32)], isClosed=True, color=(0, 255, 255), thickness=1)  # Annotate EAST (Cyan)
 
## EXECUTE INPAINTING
inpainted_image = cv2.inpaint(orig_image, inpaint_mask, inpaintRadius=5, flags=cv2.INPAINT_NS)  # All models
inpainted_db50_image = cv2.inpaint(orig_db50_image, inpaint_mask_db50, inpaintRadius=5, flags=cv2.INPAINT_NS)  # DB50 only
inpainted_db18_image = cv2.inpaint(orig_db18_image, inpaint_mask_db18, inpaintRadius=5, flags=cv2.INPAINT_NS)  # DB18 only
inpainted_east_image = cv2.inpaint(orig_east_image, inpaint_mask_east, inpaintRadius=5, flags=cv2.INPAINT_NS)  # EAST only
 
## SHOW RESULTS
cv2.imshow('Original', image)
cv2.imshow('Annotated (All Models)', annotated_image)
cv2.imshow('Inpainted (All Models)', inpainted_image)

cv2.imshow('Annotated (DB50 Only)', annotated_db50_image)
cv2.imshow('Inpainted (DB50 Only)', inpainted_db50_image)

cv2.imshow('Annotated (DB18 Only)', annotated_db18_image)
cv2.imshow('Inpainted (DB18 Only)', inpainted_db18_image)

cv2.imshow('Annotated (EAST Only)', annotated_east_image)
cv2.imshow('Inpainted (EAST Only)', inpainted_east_image)

cv2.waitKey(0)
cv2.destroyAllWindows()