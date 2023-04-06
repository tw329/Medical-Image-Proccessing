import numpy as np 
import cv2

img = cv2.imread("homework2.png", 1)
img_output = cv2.inRange(img, (0, 0, 0), (0, 0, 255))

cv2.imwrite("img_output.png", img_output)