import cv2
import numpy as np

img  = np.zeros((512,512,3),np.uint8) #ndarry로 이미지 생성 / 3개의 컬러 채널
print(img.shape)
#img[200:300,100:300]= 255,0,0 #blue [:]는 이미지 전체 설정

cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,255,0),3) # 라인 만들기 3= thickness 굵기 /width, height
cv2.rectangle(img,(0,0),(250,350),(0,0,255),cv2.FILLED) #마지막은 굵기 / 사각형 그리기 FILLED는 모두 채우기
cv2.circle(img,(400,50),30,(255,255,0),5)
cv2.putText(img," OPENCV ",(300,200),cv2.FONT_HERSHEY_COMPLEX,1,(0,150,0),2) #텍스트 쓰기/ 시작위치, 폰트 /사이즈 / 컬러 / 굵기

cv2.imshow("Image",img)

cv2.waitKey(0)