## IMPORT MODULES
import cv2
 
## LOAD IMAGE
img = cv2.imread("images/1.jpg")

## GET USER INPUT: SELECT ROI (DRAG A BOX)
roi = cv2.selectROI("Select ROI", img, False)
 
## EXTRACT CROPPED REGION
cropped_img = img[int(roi[1]):int(roi[1]+roi[3]), int(roi[0]):int(roi[0]+roi[2])]
 
## SAVE AND SHOW CROPPED IMAGE
cv2.imwrite("Cropped.png", cropped_img)
cv2.imshow("Cropped Image", cropped_img)
cv2.waitKey(0)
cv2.destroyAllWindows()