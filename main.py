import cv2

import numpy as np

# Open the first Camera:
cap = cv2.VideoCapture(0)

# if your camera is opened it sould start the process:
while cap.isOpened():
    
    # Separate video frame by frame:
    ret, frame = cap.read()
    
    # convert frame to gray:
    grayScale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # masking:
    ret, thresh = cv2.threshold(grayScale, 110, 255, cv2.THRESH_BINARY_INV)
    
    # finding the Shapes:
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # Draw on frame:
    cv2.drawContours(frame, contours, -1, (0,0,255), 3)
    
    # Shows the Video:
    cv2.imshow("Founded", frame)
    
    # Exite.
    if cv2.waitKey(1) & 0XFF == ord("q"):
        
        break
    
cv2.destroyAllWindows()
    