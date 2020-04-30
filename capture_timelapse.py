# Periodically captures images and places them in a folder

import numpy as np
frame_prefix = 'frame_'
frame_suffix = '.png'

import cv2
import os
import itertools
import math
import time
from datetime import datetime

# Timelapse Params
base_dir = './images/'
capture_dir = 'test/'
max_frames = math.inf
period = 30
#period = 0.1

# Don't take images between 5pm and 9am (when light is off)
blackout_start = 12+5
blackout_end = 0+9

## Don't take images between 5pm and 9am (when light is off)
#blackout_start = 12+10
#blackout_end = 12+11

# Max number of leading zeros, to keep things in order
if(max_frames == math.inf):
    max_places = 18
else:
    max_places = int(math.log(max_frames)/math.log(10) + 1)


# Make the directory
os.makedirs(base_dir+capture_dir, exist_ok=True)

cap = cv2.VideoCapture(0)
# Set camera resolution
cap.set(cv2.CAP_PROP_FRAME_WIDTH,1920);
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,1080);

# Exposure settings (not yet working)
#cap.set(cv2.CAP_PROP_AUTO_EXPOSURE, 0.25)
#cap.set(cv2.CAP_PROP_AUTO_EXPOSURE, 0)
#cap.set(cv2.CAP_PROP_EXPOSURE, 0.10)
#focus = 0  # min: 0, max: 255, increment:5
#cap.set(28, focus)

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
    last_time += period

    write_str = (frame_prefix+'{0:0'+str(max_places)+'d}'+frame_suffix).format(i)
    print(datetime.now().hour)
    current_hour  = datetime.now().hour
    if(current_hour > blackout_end and current_hour < blackout_start):
        cv2.imwrite(base_dir+capture_dir+write_str, frame)
        out_str = (write_str+'\tCaptured {0:-1.2f} seconds @ {1:-1.2f} frames-per-minute').format(last_time-init_time, 60/period)
    else:
        out_str = (write_str+'\tBLACKOUT {0:-1.2f} seconds @ {1:-1.2f} frames-per-minute').format(last_time-init_time, 60/period)

    print(out_str)

    ## Display the resulting frame
    #cv2.imshow('frame',frame)
    #if cv2.waitKey(1) & 0xFF == ord('q'):
    #    break


# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
