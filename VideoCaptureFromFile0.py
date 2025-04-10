## IMPORT MODULES
import cv2
import numpy as np 

## OPEN VIDEO
cap = cv2.VideoCapture("images/2.gif")
 
## CHECK IF VIDEO OPENED SUCCESSFULLY
if not cap.isOpened():
    print("Error: Could not open video file.")
else:
    print("Video file opened successfully!")
 
## READ THE FIRST FRAME TO CONFIRM READING
ret, frame = cap.read() ## ret=BOOLEAN, frame=SINGLE SCREENFRAME

## BEGIN IF / ELSE 
if ret:

    ## SHOW THE FRAME
    cv2.imshow("First Frame", frame)
    cv2.waitKey(0)  ## WAIT FOR KEYPRESS TO CLOSE WINDOW
    cv2.destroyAllWindows()  # CLOSE ALL WINDOWS
    
else:
    print("Error: Could not read the frame.")
## END IF / ELSE

## RELEASE THE VIDEO CAPTURE OBJECT
cap.release()