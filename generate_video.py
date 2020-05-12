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
skip_mult = 8

frame_files = [f for f in listdir(path) if isfile(join(path, f))]
frame_files.sort()
# Skip over `skip_mult' frames
frame_files = frame_files[::skip_mult]

frame_0 = cv2.imread(base_dir+capture_dir+frame_files[0])
frame_width = int(frame_0.shape[1])
frame_height = int(frame_0.shape[0])
out = cv2.VideoWriter(base_dir+'outpy8.avi',cv2.VideoWriter_fourcc('M','J','P','G'), fps, (frame_width,frame_height))

for idx,frame_f in enumerate(frame_files):
    frame = cv2.imread(base_dir+capture_dir+frame_f)
    out_str = ('Encoding: '+frame_f+'\t{0:3.2f}%\tFrameMean: {1:f}').format(100*idx/len(frame_files), np.mean(frame))
    print(out_str, end='\r')
    out.write(frame)


# When everything done, release the capture
out.release()
cv2.destroyAllWindows()
