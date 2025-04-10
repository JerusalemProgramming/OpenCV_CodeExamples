## IMPORT MODULES
import cv2
 
## OPEN VIDEO FILE
cap = cv2.VideoCapture("images/2.gif")
 
## CHECK IF VIDEO FILE OPENED SUCCESSFULLY
if not cap.isOpened():
    print("Error: Could not open video file.")
else:
    print("Video file opened successfully!")
 
## GET VIDEO PROPERTIES
## GET FRAME COUNT
frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))  ## GET TOTAL NUMBER OF FFRAMES IN THE VIDEO

## GET FPS
fps = cap.get(cv2.CAP_PROP_FPS)  ## GET FRAMES PER SECOND (FPS)

## GET FRAME HEIGHT
frame_height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT) ## GET FRAME HEIGHT

## GET FRAME WIDTH
frame_width = cap.get(cv2.CAP_PROP_FRAME_WIDTH) ## GET FRAME WIDTH

## TEST PRINT OUTPUT
print(f"Total frames: {frame_count}, FPS: {fps}, H = {frame_height}, W = {frame_width}")
 
## READ AND DISPLAY EACH FRAME OF THE VIDEO
while True:

    ## READ FRAME
    ret, frame = cap.read() ## ret=BOOLEAN, frame=SINGLE SCREENFRAME

    ## BEGIN IF / ELSE
    if not ret: ## BOOLEAN BECOMES FALSE AFTER THE LAST FRAME
        print("End of video or error occurred.")
        break

    ## END IF / ELSE
 
    ## SHOW THE FRAME
    cv2.imshow("Video Frame", frame)
 
    ## WAIT FOR 1ms FOR KEYPRESS TO CONTINUE OR EXIT IF q IS PRESSED
    ## BEGIN IF / ELSE
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    ## END IF/ELSE
 
## RELEASE THE VIDEO CAPTURE OBJECT AND CLOSE ANY OPENCV WINDOWS
cap.release()
cv2.destroyAllWindows()