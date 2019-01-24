import cv2 as cv
import numpy as np

mouth = np.uint8([[[156,156,156 ]]])
hsv_mouth = cv.cvtColor(mouth,cv.COLOR_BGR2HSV)
print( hsv_mouth )