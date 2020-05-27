# Periodically captures images and places them in a folder

import numpy as np
frame_prefix = 'frame_'
frame_suffix = '.jpg'

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
period = 10
jpg_quality = 98

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

# Set a manual focus (if provided)
focus = int(input('Set Manual Focus (between 0 and 255). Enter -1 for autofocus: '))
# Set the focus
if(focus > 255 or focus < 0):
    print('Autofocus Enabled')
else:
    cap.set(cv2.CAP_PROP_AUTOFOCUS, 0)
    cap.set(28, focus)

# Exposure settings (not yet working)
#cap.set(cv2.CAP_PROP_AUTO_EXPOSURE, 0.25)
#cap.set(cv2.CAP_PROP_AUTO_EXPOSURE, 0)
#cap.set(cv2.CAP_PROP_EXPOSURE, 0.10)

frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

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
    current_hour  = datetime.now().hour
    if(True):
        cv2.imwrite(base_dir+capture_dir+write_str, frame, [int(cv2.IMWRITE_JPEG_QUALITY), jpg_quality])
        out_str = (write_str+'\tCaptured {0:-1.2f} seconds @ {1:-1.2f} fpm or {2:-1.2f} fph ').format(last_time-init_time, 60/period, 60*60/period)
    else:
        out_str = (write_str+'\tCaptured {0:-1.2f} seconds @ {1:-1.2f} fpm or {2:-1.2f} fph ').format(last_time-init_time, 60/period, 60*60/period)

    print(out_str)

    ## Display the resulting frame
    #cv2.imshow('frame',frame)
    #if cv2.waitKey(1) & 0xFF == ord('q'):
    #    break


# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
