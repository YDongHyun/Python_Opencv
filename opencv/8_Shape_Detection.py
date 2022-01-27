import cv2
import numpy as np

path = 'shapes.jpg'
img = cv2.imread(path)
imgContour = img.copy() # 이미지 복사

def getContours(img):
    countours, hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE) #사진 윤곽 잡기
    for cnt in countours:
        area = cv2.contourArea(cnt)
        print(area)
        if area>500:   #자잘한거 안잡게 처리
            cv2.drawContours(imgContour, cnt, -1, (255, 0, 0), 3)  # BLUE 윤곽선 그리기
            peri = cv2.arcLength(cnt,True)
            print(peri) # 길이 출력
            approx = cv2.approxPolyDP(cnt,0.02*peri,True) #꼭지점 찾기
            print(approx)
            objCor = len(approx) #approx 개수에 따라 모양 추측

            x ,y ,w ,h = cv2.boundingRect(approx) # 도형이 있으면 사각형 박스에 넣음
            if objCor == 3: objectType = "Tri"
            elif objCor == 4:
                aspRation =w/float(h)
                if aspRation >0.95 and aspRation<1.05: objectType="Square"  #정사각형인지
                else: objectType="Rectangle"
            elif objCor>4 : objectType="circle"
            else:objectType="None"

            cv2.rectangle(imgContour,(x,y),(x+w,y+h),(0,255,0),2)# 도형이 있으면 사각형 박스에 넣음
            cv2.putText(imgContour,objectType,(x+(w//2)-10,y+(h//2)-10),
                        cv2.FONT_HERSHEY_COMPLEX,0.7,(0,0,0),2) #도형 중앙에 텍스트 출력

imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,(7,7),1)
imgCanny = cv2.Canny(imgBlur, 50, 50)
getContours(imgCanny)

imgBlank = np.zeros_like(img)

cv2.imshow("contour", imgContour)
cv2.imshow("Blur", imgBlur)
cv2.waitKey(0)