from cv2 import cv2 as cv
from detectGesture import detectGesture
import calculator
import numpy as np
import math


cam = cv.VideoCapture(0)
cam.set(cv.CAP_PROP_AUTOFOCUS, 0)

kernel = np.ones((5,5),np.uint8)
blur = (3,3)

fFrame = cv.flip(cam.read()[1], 1)
fRoi = fFrame[75:350, 75:350]
fGray = cv.cvtColor(fRoi, cv.COLOR_BGR2GRAY)
fGray = cv.GaussianBlur(fGray, blur, 0)


delay = 30
history = []
gestureSeq = []
mostCommon = ""

while(cam.isOpened):
    
    frame = cv.flip(cam.read()[1], 1)
    roi = frame[75:350, 75:350]
    gRoi = cv.cvtColor(roi, cv.COLOR_BGR2GRAY)
    gROi = cv.GaussianBlur(gRoi, blur, 0)
    cv.rectangle(frame,(75,75),(350,350),(7,205,255),0) 

    diff = cv.subtract(fGray, gRoi)
    bDiff = cv.threshold(diff, 20, 255, cv.THRESH_BINARY)[1]
    bDiff = cv.dilate(bDiff, kernel, iterations=2)

    contours = cv.findContours(bDiff, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)[0]
    if contours != []:
        hull_list = []
        for i in range(len(contours)):
            hull = cv.convexHull(contours[i])
            hull_list.append(hull)
        cv.drawContours(roi, contours, -1, (0,255,255), 1)
        cv.drawContours(roi, hull_list, -1, (48,250,17), 2)
        
        res = contours[0]
        hull = cv.convexHull(res, returnPoints=False)
        gesture = detectGesture(contours, res, hull)
        if gesture != None:
            cv.putText(roi, str(gesture), (5, 25), cv.FONT_HERSHEY_SIMPLEX, 1, (0,255,255))
        else:
            cv.putText(roi, "Unrecognized", (5, 25), cv.FONT_HERSHEY_SIMPLEX, 1, (28,28,212))


        if gesture != None:
            history.append(gesture)

        if len(history) >= delay:
            mostCommon = max(set(history), key = history.count)
            history.clear()
            if gestureSeq and not calculator.isValid(gestureSeq[-1], mostCommon):
                cv.putText(roi, "Invalid sequence", (5, 265), cv.FONT_HERSHEY_SIMPLEX, 1, (28,28,212)) #fix flicker
            else:
                gestureSeq.append(mostCommon)
            if mostCommon == "palm":
                print(calculator.calculate(gestureSeq)) #debugging
        cv.putText(roi, str(mostCommon), (5, 265), cv.FONT_HERSHEY_SIMPLEX, 1, (0,255,255)) #debugging purposes


    cv.imshow("Focus", roi)
    cv.imshow("diffroi", diff)
    cv.imshow("bin", bDiff)
    cv.imshow("Main cam", frame)





    if cv.waitKey(1) & 0xFF == ord("q"):
        break


cam.release()
cv.destroyAllWindows()
