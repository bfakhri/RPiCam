# Compiles all images in a folder to a video

import numpy as np
import cv2
import os
import itertools
import math
from os import listdir
from os.path import isfile, join


base_dir = './images/'
capture_dir = 'test/'
path = base_dir + capture_dir
fps = 60
skip_mult = 10
mean_mult = 3

frame_files = [f for f in listdir(path) if isfile(join(path, f))]
frame_files.sort()

frame_0 = cv2.imread(base_dir+capture_dir+frame_files[0])
frame_width = int(frame_0.shape[1])
frame_height = int(frame_0.shape[0])
out = cv2.VideoWriter(base_dir+'video_slider_timelapse.avi',cv2.VideoWriter_fourcc('M','J','P','G'), fps, (frame_width,frame_height))

frame_buff = []
frame_files = frame_files[::skip_mult]
for idx,frame_f in enumerate(frame_files):
    frame = cv2.imread(base_dir+capture_dir+frame_f)
    frame_buff.append(frame)
    out_str = ('Encoding: '+frame_f+'\t{0:3.2f}%').format(100*idx/len(frame_files))
    print(out_str, end='\r')
    mean_frame = np.mean(frame_buff, axis=0)
    out.write(mean_frame.astype(np.uint8))
    if(len(frame_buff) >= mean_mult):
        frame_buff.pop(0)


# When everything done, release the capture
out.release()
