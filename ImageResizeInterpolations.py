## LOAD MODULES
import cv2
 
## LOAD IMAGE
image = cv2.imread("images/1.jpg")
 
## GET ORIGINAL DIMENSIONS
height_original, width_original = image.shape[:2]

## TEST PRINT OUTPUT
print(image.shape)
 
## SCALING FACTORS FOR RESIZING
fx = 1.5
fy = 0.5
 
## APPLY DIFFERENT INTERPOLATION METHODS
resized_area = cv2.resize(image, None, fx=fx, fy=fy, interpolation=cv2.INTER_AREA)
resized_linear = cv2.resize(image, None, fx=fx, fy=fy, interpolation=cv2.INTER_LINEAR)
resized_cubic = cv2.resize(image, None, fx=fx, fy=fy, interpolation=cv2.INTER_CUBIC)
resized_nearest = cv2.resize(image, None, fx=fx, fy=fy, interpolation=cv2.INTER_NEAREST)
resized_lanczos4 = cv2.resize(image, None, fx=fx, fy=fy, interpolation=cv2.INTER_LANCZOS4)
 
## SHOW RESIZED IMAGES
## cv2.imshow("Original Image", image)
## cv2.imshow("Resized with INTER_AREA", resized_area)
cv2.imshow("Resized with INTER_LINEAR", resized_linear)
## cv2.imshow("Resized with INTER_CUBIC", resized_cubic)
## cv2.imshow("Resized with INTER_NEAREST", resized_nearest)
cv2.imshow("Resized with INTER_LANCZOS4", resized_lanczos4)
cv2.waitKey(0)
cv2.destroyAllWindows()