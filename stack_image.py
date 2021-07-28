import cv2
import numpy as np

image = cv2.imread('lena.png')

horizontal = np.hstack((image,image))
vertical = np.vstack((image,image))

cv2.imshow("Horizontal",horizontal)
cv2.imshow("Vertical",vertical)

cv2.waitKey(0)