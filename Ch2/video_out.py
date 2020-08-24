import cv2
import sys

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Camera Open failed!")
    sys.exit()

w = round(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
h = round(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
# fps = cap.get(cv2.CAP_PROP_FPS)
fps = 30

fourcc = cv2.VideoWriter_fourcc(*'DIVX') # *'DIVX' == 'D', 'I', 'V', 'X '
delay = round(1000/fps)

out = cv2.VideoWriter('output.avi', fourcc, fps, (w,h))
