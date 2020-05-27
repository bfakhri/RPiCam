import numpy as np
import cv2
import time

#cap = cv2.VideoCapture(0)
cap = cv2.VideoCapture(1)
# Set camera resolution
cap.set(cv2.CAP_PROP_FRAME_WIDTH,1920);
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,1080);
cap.set(cv2.CAP_PROP_AUTOFOCUS, 0)

focus = 0   # from 0 to 255 
direction = 1

frames_between = 10

while(True):
    focus = int(input('Set Focus to: '))
    # Set the focus
    if(focus > 255 or focus < 0):
        print('Error, focus must be between 0 and 255')
    else:
        cap.set(28, focus)

    for i in range(frames_between):
        # Capture frame-by-frame
        ret, frame = cap.read()

        # Display the resulting frame
        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
