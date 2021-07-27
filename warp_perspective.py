import cv2
import numpy as np

image = cv2.imread('cards.jpg')
width,height = 300,350 

pt_1 = np.float32([[111, 219], [287, 188], [154, 482], [352, 440]])
pt_2 = np.float32([[0, 0], [width , 0], [0, height], [width, height]])

matrix = cv2.getPerspectiveTransform(pt_1, pt_2)

image_out = cv2.warpPerspective(image,matrix,(width,height))

cv2.imshow("Original Image",image)
cv2.imshow("Warped Image",image_out)

cv2.waitKey(0)