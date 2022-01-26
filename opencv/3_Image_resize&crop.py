#opencv는 y축이 내려가는 방향임 왼쪽 위가 0,0

import cv2
import numpy as np

img = cv2.imread("C:\\Users\\user\\PycharmProjects\\python_opencv\\opencv\\test.jpg")
print(img.shape) #이미지 사이즈 출력

imgResize = cv2.resize(img, (300,200)) #width, height 순서대로 사이즈 변경
print(imgResize.shape)

imgCropped = img[0:200,200:500] #height first, width next / image crop

cv2.imshow("Image",img)
cv2.imshow("Image Resize",imgResize)
cv2.imshow("Image Cropped",imgCropped)
cv2.waitKey(0)