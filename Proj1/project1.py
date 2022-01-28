import cv2
import numpy as np

frameWidth = 1280
frameHeight = 800

cap = cv2.VideoCapture(0)#0으로 하면 웹캠 사용 가능
cap.set(3,frameWidth)
cap.set(4,frameHeight)
cap.set(10,150) #밝기 설정

myColors = [[5,107,0,19,255,255],
            [133,56,0,159,156,255],
            [57,76,0,100,255,255]]
myColorValuse = [[51,153,255],[255,0,255],[0,255,0]]

myPoints = [] # [x,y,colorId]

def findColor(img,myColors,myColorValues):
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    count = 0
    newPoints = []
    for color in myColors:
        lower = np.array(color[0:3])
        upper = np.array(color[3:6])
        mask = cv2.inRange(imgHSV, lower, upper)
        x,y = getContours(mask)
        cv2.circle(imgResult,(x,y),10,myColorValuse[count],cv2.FILLED)
        if x!=0 and y!=0:
           newPoints.append([x,y,count])
        count +=1
        #cv2.imshow(str(color[0]),mask)
    return newPoints

def getContours(img):
    countours, hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE) #사진 윤곽 잡기
    x,y,w,h = 0,0,0,0
    for cnt in countours:
        area = cv2.contourArea(cnt)
        if area>500:   #자잘한거 안잡게 처리
            #cv2.drawContours(imgResult, cnt, -1, (255, 0, 0), 3)  # BLUE 윤곽선 그리기
            peri = cv2.arcLength(cnt,True)
            approx = cv2.approxPolyDP(cnt,0.02*peri,True) #꼭지점 찾기
            x ,y ,w ,h = cv2.boundingRect(approx) # 도형이 있으면 사각형 박스에 넣음
    return x+w//2, y

def drawOnCanvas(myPoints,myColorValues):
    for point in myPoints:
        cv2.circle(imgResult,(point[0],point[1]),10,myColorValuse[point[2]],cv2.FILLED)

while True:
    success, img = cap.read()
    imgResult = img.copy()
    newPoints = findColor(img,myColors,myColorValuse)
    if len(newPoints)!=0:
        for newP in newPoints:
            myPoints.append(newP)
    if len(myPoints) != 0:
        drawOnCanvas(myPoints,myColorValuse)

    cv2.imshow("video",imgResult)
    if cv2.waitKey(1) & 0xFF==ord('q'): #q누르면 비디오 종료
        break