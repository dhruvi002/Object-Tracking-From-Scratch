import cv2
import numpy as np
from object_detection import ObjectDetection

#Initialise Object Detection
od = ObjectDetection()

cap = cv2.VideoCapture('los_angeles.mp4')

#Initialise Count
count = 0
centerPointCurrentFrame = []
centerPointPrevFrame = []

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
        centerPointCurrentFrame.append((cx,cy))

        # print("FRAME NO", count, ': ', x, y, w, h)
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0, 255, 0), 2)
        # cv2.circle(frame, (cx,cy), 5, (0,0,255), -1)

    for pt in centerPointCurrentFrame:
        cv2.circle(frame, pt, 5, (0,0,255), -1)

    #for point in centre point current frame:
    print('Current Frame: ')
    print(centerPointCurrentFrame)

    print('Previous Frame: ')
    print(centerPointPrevFrame)

    cv2.imshow('Frame', frame)

    #Make a copy of the points
    centerPointPrevFrame = centerPointCurrentFrame.copy()

    key = cv2.waitKey(1)

    if key == 27: 
        break

cap.release()
cv2.destroyAllWindows()