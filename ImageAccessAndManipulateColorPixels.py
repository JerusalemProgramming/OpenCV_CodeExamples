## IMPORT MODULES
import cv2
import matplotlib.pyplot as plt

## LOAD IMAGE 
image_path = "images/1.jpg"
img = cv2.imread(image_path)

## SHOW IMAGE
plt.imshow(img[:,:,::-1])
## plt.imshow(img, cmap='gray')

## PLOT IMAGE
plt.figure(figsize=[20,20])

img[0,0] = (0,255,255)
plt.subplot(131);plt.imshow(img[:,:,::-1])

img[1,1] = (255,255,0)
plt.subplot(132);plt.imshow(img[:,:,::-1])

img[2,2] = (255,0,255)
plt.subplot(133);plt.imshow(img[:,:,::-1])

## SHOW IMAGE
plt.show()

## TEST PRINT OUTPUT
print(img)
print(img[0,0])


