## IMPORT MODULES
import cv2
 
## DEFINE IMAGE PATH
image_path = "images/1.jpg"
 
## LOAD THE IMAGE IN DIFFERENT MODES Load the image in different modes
## DEFAULT: BGR COLOR
image_color = cv2.imread(image_path, cv2.IMREAD_COLOR) 
 
## GRAYSCALE      
image_gray = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)  
  
## AS-IS (INCLUDES ALPHA IF AVAILABLE)
image_unchanged = cv2.imread(image_path, cv2.IMREAD_UNCHANGED) 
 
## SHOW ALL IMAGES
cv2.imshow("Color Image (BGR)", image_color)
cv2.imshow("Grayscale Image", image_gray)
cv2.imshow("Unchanged Image", image_unchanged)
 
## WAIT FOR KEYPRESS TO CLOSE ALL WINDOWS
cv2.waitKey(0)
cv2.destroyAllWindows()