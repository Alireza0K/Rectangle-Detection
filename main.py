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
    ret, thresh = cv2.threshold(grayScale, 50, 255, cv2.THRESH_BINARY_INV)
    
    # finding the Shapes:
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    for contour in contours:
        
        # making edge for shape:
        approx = cv2.approxPolyDP(contour, 0.1 * cv2.arcLength(contour, True), True)
        
        # Check if edges equal the 4:
        if len(approx) == 4:
    
            # finding the edge of Rectange:
            x, y, w, h = cv2.boundingRect(approx)
            
            if (100,100) <= (w, h) <= (900, 900):
                
                # draw The rectangel on frame:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                
                # point to the center of rectangle
                cv2.circle(frame, (int(x + w / 2), int(y + h / 2)), 1, (0,0,255), 3)
                
                # put text up above the shape founded:
                cv2.putText(frame, str((w, h)), (x, y - 10),
                            cv2.FONT_HERSHEY_PLAIN, 1, (255,255,255),2)
    
    # Shows the Video:
    cv2.imshow("Founded", frame)
    
    # Exite.
    if cv2.waitKey(1) & 0XFF == ord("q"):
        
        break
    
cv2.destroyAllWindows()
    