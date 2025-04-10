## IMPORT MODULES
import cv2
import matplotlib.pyplot as plt
 
## LOAD IMAGE
img = cv2.imread("images/1.jpg")

## GET ORIGINAL DIMENSIONS
height_original, width_original = img.shape[:2]

## TEST PRINT OUTPUT
print(img.shape)
print("Data type = {}\n".format(img.dtype))
print("Object type = {}\n".format(type(img)))
print("Image Dimensions = {}\n".format(img.shape))
 
## DEFINE REGION OF INTEREST (ROI) - ARBITRARY COORDINATES
x_start, y_start, x_end, y_end = 178, 0, 366, 253  ## ADJUST AS NEEDED
 
## CROP THE IMAGE USING SLICING
cropped_img = img[y_start:y_end, x_start:x_end]
 
## SHOW IMAGE ORIGINAL
plt.imshow(img[:,:,::-1])
plt.show()

## SHOW IMAGE CROPPED
plt.imshow(cropped_img[:,:,::-1])
plt.show()

## SHOW IMAGES - ORIGNAL AND CROPPED
cv2.imshow("Original Image", img)
cv2.imshow("Cropped Image", cropped_img)
cv2.waitKey(0)
cv2.destroyAllWindows()