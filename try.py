import numpy as np
import cv2

red = np.int8([[[255, 0, 0]]])
hsv_red = cv2.cvtColor(red, cv2.COLOR_BGR2HSV)

print(hsv_red)