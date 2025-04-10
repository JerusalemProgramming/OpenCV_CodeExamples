## IMPORT MODULES
import cv2
import os
 
## LOAD IMAGE
img = cv2.imread("images/1.jpg")

## GET IMAGE DIMENSIONS
img_h, img_w, _ = img.shape
 
## PATCH SIZE
patch_w, patch_h = 100, 100  ## ADJUST AS NEEDED
 
## CREATE OUTPUT DIRETORY IF IT DOESN'T EXIST
output_dir = "patches"
os.makedirs(output_dir, exist_ok=True)
 
## COUNTER FOR PATCH NUMBERING
patch_id = 0
 
## LOOP THROUGH IMAGE ROWS WITH STEP SIZE = PATCH SIZE
for y in range(0, img_h, patch_h):

    ## LOOP THROUGH IMAGE COLUMNS WITH STEP SIZE = PATCH SIZE
    for x in range(0, img_w, patch_w):
 
        ## ENSURE PATCH DOES NOT EXCEED IMAGE BOUNDARIES
        x_end = min(x + patch_w, img_w)
        y_end = min(y + patch_h, img_h)
 
        ## CROP THE PATCH
        patch = img[y:y_end, x:x_end]
 
        ## CREATE FILE NAME
        patch_filename = f"{output_dir}/patch_{patch_id}.png"
        
        ## SAVE THE PATCH
        cv2.imwrite(patch_filename, patch)
 
        ## DRAW RECTANGLE ON ORIGINAL IMAGE (VISUALIZATION)
        cv2.rectangle(img, (x, y), (x_end, y_end), (0, 255, 0), 2)

        ## INCREMENT COUNTER
        patch_id += 1
 
## SHOW ORIGINAL IMAGE WITH DRAWN PATCHES
cv2.imshow("Patches", img)
cv2.waitKey(0)
cv2.destroyAllWindows()