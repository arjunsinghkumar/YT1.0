import cv2
import numpy as np
import glob

frameSize = (1000, 800)

out = cv2.VideoWriter('output_video.avi',cv2.VideoWriter_fourcc(*'DIVX'), 10, frameSize)

for filename in glob.glob('C:/poems/screengrab/*.png'):
    img = cv2.imread(filename)
    out.write(img)

out.release()