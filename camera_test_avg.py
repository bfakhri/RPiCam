import numpy as np
import cv2
import time

cap = cv2.VideoCapture(0)
#cap = cv2.VideoCapture(1)
# Set camera resolution
cap.set(cv2.CAP_PROP_FRAME_WIDTH,1920);
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,1080);
#cap.set(cv2.CAP_PROP_AUTOFOCUS, 0)


#focus = int(input('Enter Focus (0-255): '))
#cap.set(28, focus) 

avg_list = []

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    avg_list.append(frame)
    if(len(avg_list) > 30):
        avg_list.pop(0)

    # Our operations on the frame come here
    print(len(avg_list))

    # Display the resulting frame
    #cv2.imshow('frame',gray)
    show_frame = np.mean(np.stack(avg_list, axis=0), axis=0).astype(np.uint8)
    print(show_frame.shape, frame.dtype)
    cv2.imshow('avg', show_frame)
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
