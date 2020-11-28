from cv2 import cv2 as cv
import numpy as np
import math


#BASE IDEA
# Simple calculator with input parsed from hand gestures
# Small interval to combine numbers (wait until combine sign)

#SUPPORT FOR FOLLOWING GESTURES
# 0-5 numbers (0 as "ok"-sign or similar)
# fist for COMBINE gesture, e.g. 3+5 = 8 - parsed with some small interval 3s, or something
# something as + and - gestures
# something as / and * gestures
# NEXT gesture, e.g. 3 -> "next" -> 6 = 36
# something as CALCULATE gesture
# RESET and #REWIND gestures



cam = cv.VideoCapture(0)

kernel = np.ones((5,5),np.uint8)
blur = (3,3)

fFrame = cv.flip(cam.read()[1], 1)
fRoi = fFrame[75:350, 75:350]
fGray = cv.cvtColor(fRoi, cv.COLOR_BGR2GRAY)
fGray = cv.GaussianBlur(fGray, blur, 0)


while(cam.isOpened):
    
    frame = cv.flip(cam.read()[1], 1)
    roi = frame[75:350, 75:350]
    gRoi = cv.cvtColor(roi, cv.COLOR_BGR2GRAY)
    gROi = cv.GaussianBlur(gRoi, blur, 0)
    cv.rectangle(frame,(75,75),(350,350),(7,205,255),0) 
    cv.imshow("Main cam", frame)

    diff = cv.subtract(fGray, gRoi)
    bDiff = cv.threshold(diff, 20, 255, cv.THRESH_BINARY)[1]
    bDiff = cv.dilate(bDiff, kernel, iterations=2)

    contours = cv.findContours(bDiff, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)[0]
    if contours != []:
        #contour with highest area
        #handContour = max(contours, key = lambda x: cv.contourArea(x))
        hull_list = []
        for i in range(len(contours)):
            hull = cv.convexHull(contours[i])
            hull_list.append(hull)
        cv.drawContours(roi, contours, -1, (0,255,255), 1)
        cv.drawContours(roi, hull_list, -1, (48,250,17), 2)
        
        res = contours[0]
        hull = cv.convexHull(contours[0], returnPoints=False)
        if len(hull) > 3: #source https://github.com/lzane/Fingers-Detection-using-OpenCV-and-Python
            defects = cv.convexityDefects(res, hull)
            if type(defects) != type(None):  # avoid crashing.   (BUG not found)

                cnt = 1
                for i in range(defects.shape[0]):  # calculate the angle
                    s, e, f, d = defects[i][0]
                    start = tuple(res[s][0])
                    end = tuple(res[e][0])
                    far = tuple(res[f][0])
                    a = math.sqrt((end[0] - start[0]) ** 2 + (end[1] - start[1]) ** 2)
                    b = math.sqrt((far[0] - start[0]) ** 2 + (far[1] - start[1]) ** 2)
                    c = math.sqrt((end[0] - far[0]) ** 2 + (end[1] - far[1]) ** 2)
                    angle = math.acos((b ** 2 + c ** 2 - a ** 2) / (2 * b * c))  # cosine theorem
                    if angle <= math.pi / 2:  # angle less than 90 degree, treat as fingers
                        cnt += 1
                        cv.circle(roi, far, 8, [211, 84, 0], -1)
                cv.putText(roi, str(cnt), (5, 25), cv.FONT_HERSHEY_SIMPLEX, 1, (0,255,255))

        #TODO 
        #cover fist/palm detection with palm https://github.com/Sadaival/Hand-Gestures/blob/master/gesture.py
        #Add template hand position
        #move hand detection stuff to functions

 

    cv.imshow("Focus", roi)
    cv.imshow("diffroi", diff)
    cv.imshow("bin", bDiff)





    if cv.waitKey(1) & 0xFF == ord("q"):
        break


cam.release()
cv.destroyAllWindows()
