import numpy as np
import cv2
import time

#cap = cv2.VideoCapture(0)
cap = cv2.VideoCapture(1)
# Set camera resolution
#cap.set(cv2.CAP_PROP_FRAME_WIDTH,1920);
#cap.set(cv2.CAP_PROP_FRAME_HEIGHT,1080);
cap.set(cv2.CAP_PROP_AUTOFOCUS, 0)


focus = int(input('Enter Focus (0-255): '))
cap.set(28, focus) 

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    print(frame.shape, focus)

    # Display the resulting frame
    #cv2.imshow('frame',gray)
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
