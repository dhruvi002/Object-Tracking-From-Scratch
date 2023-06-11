import cv2
import numpy as np
from object_detection import ObjectDetection

#Initialise Object Detection
od = ObjectDetection()

cap = cv2.VideoCapture('los_angeles.mp4')

#Initialise Count
count = 0
centerPoint = []

while True: 
    ret, frame = cap.read()

    count +=1

    if not ret: 
        break

    #Detect objects on frame 
    (class_ids, scores, boxes) = od.detect(frame)
    for box in boxes: 
        (x,y,w,h) = box

        cx = int((x+x+w)/2)
        cy = int((y+y+h)/2)
        centerPoint.append((cx,cy))

        print("FRAME NO", count, ': ', x, y, w, h)
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0, 255, 0), 2)
        # cv2.circle(frame, (cx,cy), 5, (0,0,255), -1)

    for pt in centerPoint:
        cv2.circle(frame, pt, 5, (0,0,255), -1)


    cv2.imshow('Frame', frame)
    key = cv2.waitKey(1)

    if key == 27: 
        break

cap.release()
cv2.destroyAllWindows()