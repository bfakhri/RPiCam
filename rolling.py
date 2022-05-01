import numpy as np
import cv2

#w = 1440
#h = 2560
w = 1080
h = 1920

#img = (np.random.rand(h, w)*255).astype(np.uint8)
lines = [np.random.rand(1, w, 3) for _ in range(h)]


while(True):
    img = np.vstack(lines)
    cv2.imshow('frame', img)
    cv2.waitKey(1)

    lines.append(np.random.rand(1, w, 3))
    lines.pop(0)

