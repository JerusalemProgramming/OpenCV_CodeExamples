## IMPORT MODULES
import cv2
 
## OPEN DEFAULT WEBCAM: (0)
cap = cv2.VideoCapture(0)
 
## CHECK IF WEBCAM OPENED SUCCESSFULLY
if not cap.isOpened():
    print("Error: Could not access the webcam.")
else:
    print("Webcam accessed successfully!")
 
## READ FIRST FRAME TO CONFIRM CAPTURE
ret, frame = cap.read()
 
## BEGIN IF / ELSE
if ret:
 
    ## SHOW THE FRAME
    cv2.imshow("Captured Frame", frame)
    cv2.waitKey(0)  ## WAIT FOR KEYPRESS TO CLOSE WINDOW
    cv2.destroyAllWindows()  ## CLOSE ALL WINDOWS
else:
    print("Error: Could not capture a frame.")
## END IF / ELSE
 
## RELEASE THE WEBCAM/VIDEO CAPTURE OBJECT
cap.release()