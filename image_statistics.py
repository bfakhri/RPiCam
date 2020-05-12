import numpy as np
import cv2
import matplotlib.pyplot as plt
from matplotlib import colors
from matplotlib.ticker import PercentFormatter

from os import listdir
from os.path import isfile, join


base_dir = './images/'
capture_dir = 'test/'
path = base_dir + capture_dir
frame_files = [f for f in listdir(path) if isfile(join(path, f))]
frame_files.sort()

means = []
for idx,frame_f in enumerate(frame_files[::10]):
#for idx,frame_f in enumerate(frame_files):
    frame = cv2.imread(base_dir+capture_dir+frame_f)
    mean = np.mean(frame)
    means.append(mean)
    out_str = ('Encoding: '+frame_f+'\t{0:3.2f}%\tFrameMean: {1:f}').format(100*idx/len(frame_files), mean)
    print(out_str, end='\r')

fig, axs = plt.subplots(1, 2, sharey=True, tight_layout=True)

# We can set the number of bins with the `bins` kwarg
axs[0].hist(means)
axs[1].plot(means)
plt.show()

input('wait')
