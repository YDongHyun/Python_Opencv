import cv2
import numpy as np

img = cv2.imread("C:\\Users\\user\\PycharmProjects\\python_opencv\\opencv\\test.jpg")
kernel = np.ones((5,5),np.uint8) # uint8 = 0~255까지

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # BGR순으로 되있음 / 흑백으로 만듬
imgBlur = cv2.GaussianBlur(imgGray,(7,7),0) # 커널사이즈? /sigmax=0 / 블러 처리
imgCanny = cv2.Canny(img, 150, 100) #라인만 가져옴 / 가중치
imgDialation = cv2.dilate(imgCanny,kernel, iterations=1) #팽창
imgEroded = cv2.erode(imgDialation,kernel,iterations=1) # 팽창한것을 다시 수축

cv2.imshow("Gray Image",imgGray)
cv2.imshow("Blur Image",imgBlur)
cv2.imshow("img Canny",imgCanny)
cv2.imshow("img Dialation",imgDialation)
cv2.imshow("img Eroded",imgEroded)
cv2.waitKey(0)