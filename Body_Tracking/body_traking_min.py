import cv2
import mediapipe as mp
import time

mpDraw = mp.solutions.drawing_utils
mpPose = mp.solutions.pose
pose = mpPose.Pose()

cap = cv2.VideoCapture('sampleVid/vid1.mp4')

pTime = 0
while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) #이미지 변환
    results = pose.process(imgRGB)  #포즈감지 가능 (cpu사용하므로 프레임 감소)
    print(results.pose_landmarks) #모델의 랜드마크 프린트
    if results.pose_landmarks:
        mpDraw.draw_landmarks(img, results.pose_landmarks,mpPose.POSE_CONNECTIONS) #랜드마크를 그림 점으로 표시

    cTime = time.time()
    fps = 1/(cTime-pTime) #프레임
    pTime = cTime
    cv2.putText(img,str(int(fps)),(70,50),cv2.FONT_HERSHEY_TRIPLEX,3,(255,0,255),3) #프레임 표시
    cv2.imshow("video", img)
    cv2.waitKey(1)