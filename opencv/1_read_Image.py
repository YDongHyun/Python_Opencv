import cv2

print("Package Imported")

img = cv2.imread("./opencv/test.jpg") #이미지 불러오기

cv2.imshow("Output", img) #이미지 출력
cv2.waitKey(0) #화면 켜있는 시간. 0은 무한