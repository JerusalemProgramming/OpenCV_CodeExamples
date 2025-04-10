## IMPORT MODULES
import cv2
 
## DEFINE IMAGE PATH
image = cv2.imread("images/1.jpg")
 
## SAVE COPY TO DISK AS ANOTHER FILE NAME
cv2.imwrite("images/2.jpg", image)
 
## OPTIONAL: SHOW IMAGE
cv2.imshow("Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()