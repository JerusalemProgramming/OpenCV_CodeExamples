## IMPORT MODULES
import cv2
 
## LOAD IMAGES
image = cv2.imread("images/1.jpg")
 
## DISPLAY IMAGE IN WINDOW
cv2.imshow("Displayed Image", image)
 
## WAIT FOR KEY PRESS BEFORE CLOSING WINDOW
cv2.waitKey(0)
cv2.destroyAllWindows()