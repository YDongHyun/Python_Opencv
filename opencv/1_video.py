import cv2

cap = cv2.VideoCapture(0)#0으로 하면 웹캠 사용 가능
cap.set(3,640)
cap.set(4,480)
cap.set(10,100) #밝기 설정

while True:
    success, img = cap.read()
    cv2.imshow("video",img)
    if cv2.waitKey(1) & 0xFF==ord('q'): #q누르면 비디오 종료
        break