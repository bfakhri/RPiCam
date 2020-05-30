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
fps = 30
#skip_mult = 18
mean_mult = 60
# Limit to cut night off at
min_img_mean = 10

frame_files = [f for f in listdir(path) if isfile(join(path, f))]
frame_files.sort()

frame_0 = cv2.imread(base_dir+capture_dir+frame_files[0])
frame_width = int(frame_0.shape[1])
frame_height = int(frame_0.shape[0])
out = cv2.VideoWriter(base_dir+'video_mean_timelapse.avi',cv2.VideoWriter_fourcc('M','J','P','G'), fps, (frame_width,frame_height))

frame = cv2.imread(base_dir+capture_dir+frame_files[0])
mean_frame = np.zeros_like(frame).astype(np.float32)
mean_cnt = 0
for idx,frame_f in enumerate(frame_files):
    frame = cv2.imread(base_dir+capture_dir+frame_f)
    mean = np.mean(frame)
    out_str = ('Encoding: '+frame_f+'\t{0:3.2f}%\tFrameMean: {1:f}').format(100*idx/len(frame_files), mean)
    print(out_str, end='\r')
    if(mean > min_img_mean):
        mean_frame += frame
        mean_cnt += 1
        if(mean_cnt >= mean_mult):
            mean_frame /= mean_mult
            out.write(mean_frame.astype(np.uint8))
            mean_frame = np.zeros_like(mean_frame)
            mean_cnt = 0
    else:
        print('skipping frame, too dark')


# When everything done, release the capture
out.release()
cv2.destroyAllWindows()
