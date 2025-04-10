import cv2
 
## OPEN VIDEO FILE
cap = cv2.VideoCapture("images/2.gif")
 
## CHECK IF VIDEO FILE OPENED SUCCESSFULLY
if not cap.isOpened():
    print("Error: Could not open video file.")
    exit()
 
## GET VIDEO PROPERTIES
## GET FRAME COUNT
frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))  ## GET TOTAL NUMBER OF FFRAMES IN THE VIDEO

## GET FPS
fps = cap.get(cv2.CAP_PROP_FPS)  ## GET FRAMES PER SECOND (FPS)

## GET FRAME WIDTH
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))

## GET FRAME HEIGHT
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
 
## TEST PRINT OUTPUT
print(f"Total frames: {frame_count}, FPS: {fps}, H = {frame_height}, W = {frame_width}")

## BEGIN WHILE LOOP FOR EACH FRAME
while True:

    ## READ FRAME
    ret, frame = cap.read()
    if not ret: ## if (ret == False)
        print("End of video or error occurred.")
        break

    ## SHOW FRAME
    cv2.imshow("Frame", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

## END WHILE LOOP FOR EACH FRAME
 
## RELEASE EVERYTHING
cap.release()
cv2.destroyAllWindows()