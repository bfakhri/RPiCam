# Periodically captures images and places them in a folder

import numpy as np
frame_prefix = 'frame_'
frame_suffix = '.jpg'

import cv2
import os
import itertools
import math
import time
import sys
from datetime import datetime

# Timelapse Params
base_dir = './images/'
capture_dir = 'test/'
max_frames = math.inf
jpg_quality = 98

# Frame time window (seconds compiled to one frame)
frame_duration = 2
# How often (seconds) to compile/write out a frame from the frame buffer
period = 1
# Holds frames to be compiled
frame_buffer = []

# Max number of leading zeros, to keep things in order
if(max_frames == math.inf):
    max_places = 18
else:
    max_places = int(math.log(max_frames)/math.log(10) + 1)


# Make the directory
os.makedirs(base_dir+capture_dir, exist_ok=True)

# Open the camera
cap = cv2.VideoCapture(-1)
print('CAP: ', cap)

# Get framerate from the capture device
capture_framerate = cap.get(cv2.CAP_PROP_FPS)
max_buffer_len = int(capture_framerate*frame_duration)

# Set camera resolution
cap.set(cv2.CAP_PROP_FRAME_WIDTH,1920);
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,1080);

# Exposure settings (not yet working)
#cap.set(cv2.CAP_PROP_AUTO_EXPOSURE, 0.25)
#cap.set(cv2.CAP_PROP_AUTO_EXPOSURE, 0)
#cap.set(cv2.CAP_PROP_EXPOSURE, 0.10)

frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

# Test if camera is working
ret, frame = cap.read()
if(frame is None):
    print('Reading a frame failed')
    sys.exit(1)

# Get time in seconds
last_time = time.time()
init_time = last_time

for i in itertools.count():
    if(i > max_frames-1):
        print('Done Capturing!')
        break

    # Capture frame-by-frame
    ret, frame = cap.read()

    # Process frame
    frame = frame.astype(np.float32)/255.0

    # Add frame to frame buffer
    frame_buffer.append(frame)
    
    # Trim buffer if it is too large
    if(len(frame_buffer) > max_buffer_len):
        frame_buffer.pop(0)

    #print('buffer len: ', len(frame_buffer), '\tMax buffer len: ', max_buffer_len)

    # Compile and write out frame if enough time has passed
    if(time.time() - last_time > period):
        last_time = time.time()
        out_frame = np.mean(np.stack(frame_buffer, axis=0), axis=0)
        # Turn it into something we can write out
        out_frame = (out_frame*255.0).astype(np.uint8)

        ## Display the resulting frame
        #cv2.imshow('frame',out_frame)
        #if cv2.waitKey(1) & 0xFF == ord('q'):
        #    break

        print('out frame: ', out_frame.shape, '\tmean: ', np.mean(out_frame))
        write_str = (frame_prefix+'{0:0'+str(max_places)+'d}'+frame_suffix).format(i)
        current_hour  = datetime.now().hour
        if(True):
            cv2.imwrite(base_dir+capture_dir+write_str, out_frame, [int(cv2.IMWRITE_JPEG_QUALITY), jpg_quality])
            out_str = (write_str+'\tCaptured {0:-1.2f} seconds @ {1:-1.2f} fpm or {2:-1.2f} fph ').format(last_time-init_time, 60/period, 60*60/period)
        else:
            out_str = (write_str+'\tCaptured {0:-1.2f} seconds @ {1:-1.2f} fpm or {2:-1.2f} fph ').format(last_time-init_time, 60/period, 60*60/period)

        print(out_str)



# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
