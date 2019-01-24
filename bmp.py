import numpy as np
import cv2
from matplotlib import pyplot as plt
img = cv2.imread('C:\\Users\\tfcandy\\Desktop\\19321_image\\image\\BMELabIII2DSLab1\\CGFaceGrayscale.bmp', cv2.IMREAD_COLOR)
# plt.imshow(img, cmap='gray')
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
plt.imshow(hsv)

lower_blue = np.array([0,0,156])
upper_blue = np.array([0,0,156])

mask = cv2.inRange(hsv, lower_blue, upper_blue)

res = cv2.bitwise_and(img,img, mask= mask)



plt.figure(1)
plt.imshow(img)
#plt.figure(2)
#plt.imshow(mask)
plt.figure(3)
plt.imshow(res)
#plt.figure(4)
#plt.imshow(rec)
plt.show()