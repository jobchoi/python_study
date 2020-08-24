import sys
import cv2

# 카메라  열기
# cap = cv2.VideoCapture(0) # 인자값으로 0을 주면 아래코드가 생략됨 
# 동영상파일 열기
cap = cv2.VideoCapture('video1.mp4') 
# cap.open(0)

if not cap.isOpened():
    print("Camera open failed!")
    sys.exit

while True:
    ret, frame = cap.read()
    if not ret:
        break;

    edge = cv2.Canny(frame, 50, 150)

    cv2.imshow('frame',frame)
    cv2.imshow('edge', edge)
    # cv2.imshow('frame', frame)
    if cv2.waitKey(20) == 27: # 27 == ESC
        break
cap.release()
cap.destroyAllWindows()




# # 카메라 프레임 크기 출력
# print('Frame width : ', int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)))
# print('Frame height : ', int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
