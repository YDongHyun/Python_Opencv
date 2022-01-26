import cv2
import numpy as np

img =cv2.imread("C:\\Users\\user\\PycharmProjects\\python_opencv\\opencv\\test.jpg")

imgHor = np.hstack((img, img)) #사진 옆에 붙임
imgVer = np.vstack((img,img)) # 사진 아래로 붙임

cv2.imshow("Horizontal",imgHor)
cv2.imshow("vertical",imgVer)

cv2.waitKey(0)