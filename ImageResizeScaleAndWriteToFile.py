## IMPORT MODULES
import cv2
 
## LOAD IMAGE
image = cv2.imread("images_originals/1.jpg")

## GET ORIGINAL DIMENSIONS
HeightOriginal, WidthOriginal = image.shape[:2]

## TEST PRINT OUTPUT
print(image.shape)
 
## SCALING FACTORS FOR RESIZING
ScaleDown = 0.5  
ScaleUp = 1.25    
 
## RESIZE IMAGE (SCALE DOWN)
ImageFrameResizedDown = cv2.resize(image, None, fx=ScaleDown, fy=ScaleDown, interpolation=cv2.INTER_LINEAR)
 
## RESIZE IMAGE (SCALE UP)
ImageFrameResizedUp = cv2.resize(image, None, fx=ScaleUp, fy=ScaleUp, interpolation=cv2.INTER_LINEAR)

## GET NEW DIMENSIONS FOR EACH RESIZED IMAGE
ImageFrameResizedDownHeight, ImageFrameResizedDownWidth = ImageFrameResizedDown.shape[:2]
ImageFrameResizedUpHeight, ImageFrameResizedUpWidth = ImageFrameResizedUp.shape[:2]

## TEST PRINT OUTPUT
print(f"OLD DIMENSIONS: H = {HeightOriginal}, W = {WidthOriginal}")
print(f"RESIZED DOWN DIMENSIONS: H = {ImageFrameResizedDownHeight}, W = {ImageFrameResizedDownWidth}")
print(f"RESIZED UP DIMENSIONS: H = {ImageFrameResizedUpHeight}, W = {ImageFrameResizedUpWidth}")

## SAVE COPY TO DISK AS ANOTHER FILE NAME
cv2.imwrite("images/1copy.jpg", image)
cv2.imwrite("images/1copy_resized_down.jpg", ImageFrameResizedDown)
cv2.imwrite("images/1copy_resized_up.jpg", ImageFrameResizedUp)

## SHOW IMAGES
## cv2.imshow("Original Image", image)
## cv2.imshow("Scaled Down Image", ImageFrameResizedDown)
## cv2.imshow("Scaled Up Image", ImageFrameResizedUp)
cv2.waitKey(0)
cv2.destroyAllWindows()