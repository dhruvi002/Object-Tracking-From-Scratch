import cv2
import numpy as np
from object_detection import ObjectDetection
import math

#Initialise Object Detection
od = ObjectDetection()

cap = cv2.VideoCapture('los_angeles.mp4')

#Initialise Count
count = 0
centerPointPrevFrame = []
trackingObj = {}
trackId = 0

while True: 
    ret, frame = cap.read()
    count +=1
    if not ret: 
        break

    #Point Current Frame    
    centerPointCurrentFrame = []
 
    #Detect objects on frame 
    (class_ids, scores, boxes) = od.detect(frame)
    for box in boxes: 
        (x,y,w,h) = box

        cx = int(x + 0.5*w)
        cy = int(y + 0.5*h)
        centerPointCurrentFrame.append((cx,cy))

        # print("FRAME NO", count, ': ', x, y, w, h)
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0, 255, 0), 2)
        # cv2.circle(frame, (cx,cy), 5, (0,0,255), -1)

    # for pt in centerPointCurrentFrame:
    #     cv2.circle(frame, pt, 5, (0,0,255), -1)
    
    #We compare previous and current frame only at the beginning
    
    if count <= 2 : 
        for pt in centerPointCurrentFrame:
            for pt2 in centerPointPrevFrame:
                distance = math.hypot(pt2[0] - pt[0], pt2[1] - pt[1])

                if distance < 20:
                    trackingObj[trackId] = pt
                    trackId+=1 
    else: 
        for pt in centerPointCurrentFrame:
            for pt2 in trackingObj.values():
                distance = math.hypot(pt2[0] - pt[0], pt2[1] - pt[1])
                
                if distance < 20: 
                    trackingObj[objectId] = pt  

    for objectId, ptTrackObj in trackingObj.items():
        cv2.circle(frame, (cx,cy), 5, (0,0,255), -1)
        cv2.putText(frame, str(objectId), (ptTrackObj[0], ptTrackObj[1] -7), 0, 0.5, (0,0, 255), 1)
        # print(objectId, ptTrackObj)

    print('Tracking Object: ', trackingObj)                

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
