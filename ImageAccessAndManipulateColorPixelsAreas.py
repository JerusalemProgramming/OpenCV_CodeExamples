## IMPORT MODULES
import cv2
import matplotlib.pyplot as plt
 
## OPEN IMAGE FILE
image_path = "images/1.jpg"

## READ IMAGE FILE
img = cv2.imread(image_path)

## ACCESS AND MANIPULATE AREAS OF COLOR PIXELS
img[0:3,0:3] = (255,0,0)
img[3:6,0:3] = (0,255,0)
img[6:9,0:3] = (0,0,255)

## SHOW IMAGE
plt.imshow(img[:,:,::-1])
plt.show()