# Compiles all images in a folder to a video

import numpy as np
import cv2
import os
import itertools
import math
from os import listdir
from os.path import isfile, join


base_dir = './'
#capture_dir = '../inbox/converted/'
capture_dir = '../albums/04-08-22_SunsetTimelapse/'
path = base_dir + capture_dir
vid_fps = 60
skip_mult = 1
mean_mult = 1 

frame_files = [f for f in listdir(path) if isfile(join(path, f))]
frame_files.sort()

print(frame_files)

frame_0 = cv2.imread(base_dir+capture_dir+frame_files[0])
#frame_width = int(frame_0.shape[1])
#frame_height = int(frame_0.shape[0])
frame_width = int(1920*2)
frame_height = int(1080*2)
out = cv2.VideoWriter(base_dir+'timelapse.avi',cv2.VideoWriter_fourcc('M','J','P','G'), vid_fps, (frame_width,frame_height))
#out = cv2.VideoWriter(base_dir+'timelapse.webm',cv2.VideoWriter_fourcc(*'VP90'), vid_fps, (frame_width,frame_height))
#out = cv2.VideoWriter(base_dir+'timelapse.mp4',cv2.VideoWriter_fourcc(*'VP90'), vid_fps, (frame_width,frame_height))

print('Generating a timelapse with {0} frames and a length of {1} seconds'.format(len(frame_files)//skip_mult, len(frame_files)//skip_mult/vid_fps))

frame_buff = []
sigma = 2
mu = 0
for idx,frame_f in enumerate(frame_files):
    frame = cv2.imread(base_dir+capture_dir+frame_f)
    if(frame is None):
        continue
    frame = cv2.resize(frame, (frame_width, frame_height))
    frame_buff.append(frame)
    out_str = ('Encoding: '+frame_f+'\t{0:3.2f}%').format(100*idx/len(frame_files))
    print(out_str, end='\r')
    if(idx % skip_mult == 0):
        mean_frame = np.mean(frame_buff, axis=0)
        # ADD NOISE TO REDUCE COMPRESSSION 
        mean_frame += sigma*np.random.randn(frame_height, frame_width, 1) + mu
        mean_frame = np.clip(mean_frame, 0, 2**8-1)
        out.write(mean_frame.astype(np.uint8))
    if(len(frame_buff) >= mean_mult):
        frame_buff.pop(0)



# When everything done, release the capture
out.release()
