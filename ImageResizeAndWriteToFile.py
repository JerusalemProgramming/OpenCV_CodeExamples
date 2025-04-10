## IMPORT MODULES
import cv2
 
## LOAD IMAGE
frame = cv2.imread("images/1.jpg")

## GET ORIGINAL DIMENSIONS
height_original, width_original = frame.shape[:2]

## TEST PRINT OUTPUT
print(frame.shape)
 
## DEFINE NEW WIDTH AND HEIGHT WHILE MAINTAINING ASPECT RATIO
width_new = 162
## height_new = 500

aspect_ratio = width_new / width_original
height_new = int(height_original * aspect_ratio) ## COMPUTE HEIGHT BASED ON ASPECT RATIO
 
## RESIZE IMAGE
frame_resized = cv2.resize(frame, (width_new, height_new))
 
## TEST PRINT OUTPUT
print(f"OLD DIMENSIONS: H = {height_original}, W = {width_original}")
print(f"NEW DIMENSIONS: H = {height_new}, W = {width_new}")

## SAVE COPY TO DISK AS ANOTHER FILE NAME
cv2.imwrite("images/1copy.jpg", frame_resized)
 
## SHOW RESIZED IMAGE
cv2.imshow("Resized Image", frame_resized)
cv2.waitKey(0)
cv2.destroyAllWindows()

 