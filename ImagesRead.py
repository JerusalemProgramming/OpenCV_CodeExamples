## IMPORT MODULES
import cv2
 
## LOAD IMAGES w/ COLOR MODE
image1 = cv2.imread("C:/opencv/MainRootFolder/images/1.jpg", cv2.IMREAD_COLOR)
image2 = cv2.imread("C:/opencv/MainRootFolder/images/1.jpg", cv2.IMREAD_GRAYSCALE)
image3 = cv2.imread("C:/opencv/MainRootFolder/images/1.jpg", cv2.IMREAD_UNCHANGED)
 
## CHECK IF IMAGE LOADED SUCCESSFULLY
if image1 is None:
    print("Error: Image not found or unable to read.")
else:
    print("Image loaded successfully!")
if image2 is None:
    print("Error: Image not found or unable to read.")
else:
    print("Image loaded successfully!")
if image3 is None:
    print("Error: Image not found or unable to read.")
else:
    print("Image loaded successfully!")