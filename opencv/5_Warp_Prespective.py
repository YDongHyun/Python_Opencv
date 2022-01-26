import cv2
import numpy as np

#점을 찍어 사선을 직선으로 보이게함

img =  cv2.imread("C:\\Users\\user\\PycharmProjects\\python_opencv\\opencv\\test.jpg")

width, height = 250, 350
pts1 = np.float32([[111,219],[287,188],[154,482],[352,440]]) #찍은 점
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
matrix = cv2.getPerspectiveTransform(pts1,pts2)
imgOutput = cv2.warpPerspective(img,matrix,(width,height))

cv2.imshow("image",img)
cv2.imshow("Output",imgOutput)
cv2.waitKey(0)