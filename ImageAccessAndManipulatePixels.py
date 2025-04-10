## IMPORT MODULES
import cv2
import matplotlib.pyplot as plt
 
## LOAD IMAGE
image_path = "images/1.jpg"
img = cv2.imread(image_path,0)

## TEST PRINT OUTPUT
print(img)
print("Data type = {}\n".format(img.dtype))
print("Object type = {}\n".format(type(img)))
print("Image Dimensions = {}\n".format(img.shape))

## MANIPULATE PIXELS
## img[0,0]=255
## img[1,1]=200
## img[0,2]=150

## MANIPULATE GROUPS OF PIXELS
img[0:2,0:3] = 180

## TEST PRINT OUTPUT
print(f"Pixel Color: {img[0,0]}")
print(f"Pixel Color: {img[1,1]}")
print(f"Pixel Color: {img[2,2]}")
print(img)

roi = img[0:2,0:4]
print(f"ROI: {roi}")
print(img)

## IMAGE PLOT
plt.imshow(img, cmap='gray')
plt.show()
print(img)

