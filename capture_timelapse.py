# Periodically captures images and places them in a folder

import numpy as np
frame_prefix = 'frame_'
frame_suffix = '.png'

import cv2
import os
import itertools
import math
import time


base_dir = './images/'
capture_dir = 'test/'
#max_frames = 150
max_frames = math.inf
period = 1
# Max number of leading zeros, to keep things in order
if(max_frames == math.inf):
    max_places = 16
else:
    max_places = int(math.log(max_frames)/math.log(10) + 1)


# Make the directory
os.makedirs(base_dir+capture_dir, exist_ok=True)

cap = cv2.VideoCapture(0)
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

frame_prefix = 'frame_'
frame_suffix = '.png'

# Get time in seconds
last_time = time.time()
init_time = last_time

for i in itertools.count():
    if(i > max_frames-1):
        print('Done Capturing!')
        break

    while(time.time() < last_time + period):
        time.sleep(1)

    # Capture frame-by-frame
    ret, frame = cap.read()
    last_time = time.time()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Format the output string to make it readable
    write_str = (frame_prefix+'{0:0'+str(max_places)+'d}'+frame_suffix).format(i)
    cv2.imwrite(base_dir+capture_dir+write_str, frame)
    out_str = (write_str+'\tCaptured {0:-1.2f} seconds').format(last_time-init_time)
    print(out_str)

    # Display the resulting frame
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
