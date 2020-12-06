from cv2 import cv2 as cv
from detectGesture import detectGesture
from gestures import *
import calculator
import validator
import numpy as np
import math


cam = cv.VideoCapture(0)
#cam = cv.VideoCapture(path) sample video
cam.set(cv.CAP_PROP_AUTOFOCUS, 0)

kernel = np.ones((5,5),np.uint8)
blur = (3,3)

fFrame = cv.flip(cam.read()[1], 1)
fRoi = fFrame[75:350, 75:350]
fGray = cv.cvtColor(fRoi, cv.COLOR_BGR2GRAY)
fGray = cv.GaussianBlur(fGray, blur, 0)


delay = 80
history = []
gestureSeq = []
mostCommon = ""
prev = "Operation"
chain = []
calculated = False
font = cv.FONT_HERSHEY_SIMPLEX


while(cam.isOpened):
    
    frame = cv.flip(cam.read()[1], 1)
    roi = frame[75:350, 75:350]
    gRoi = cv.cvtColor(roi, cv.COLOR_BGR2GRAY)
    gROi = cv.GaussianBlur(gRoi, blur, 0)
    cv.rectangle(frame,(74,74),(350,350),(7,205,255),0)
    cv.rectangle(roi, (0,75), (130,220),(7,205,255),0) 

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
            cv.putText(roi, str(gesture), (5, 25), font, 1, (0,255,255))
        else:
            cv.putText(roi, "Unrecognized", (5, 25), font, 1, (28,28,212))
        if gesture != None:
            history.append(gesture)
            if len(history) >= delay:
                mostCommon = max(set(history), key = history.count)
                history.clear()
                if len(gestureSeq) >= 2 and mostCommon == "rock": #TODO move above/skip passing "rock" to calculator
                    prosSeq = calculator.createSeq(gestureSeq)
                    if prosSeq:
                        total = calculator.calculateTotal(prosSeq)
                        cv.putText(roi, str(total), (5, 265), font, 1, (255,0,0))
                    calculated = True
                if prev == "Operation":
                    if not chain and isinstance(mostCommon, int):
                        chain.append(mostCommon)
                    elif len(chain) == 1 and isinstance(chain[0], int) and isinstance(mostCommon, str) and mostCommon != Calc:
                        chain.append(mostCommon)
                    elif len(chain) == 2 and isinstance(chain[0], int) and isinstance(chain[1], str) and chain[1] != Calc and isinstance(mostCommon, int):
                        chain.append(mostCommon)
                        prev, valid = validator.isValid(prev, chain)
                        gestureSeq.extend(chain)
                        chain = []
                    else:
                        cv.putText(roi, "Invalid sequence", (5, 265), font, 1, (28,28,212)) 
                elif prev == "Number":
                    prev, valid = validator.isValid(prev, mostCommon)
                    if valid:
                            gestureSeq.append(mostCommon)
                            chain = []
                else:
                    cv.putText(roi, "Invalid sequence", (5, 265), font, 1, (28,28,212))
            cv.putText(roi, str(mostCommon), (5, 265), font, 1, (0,255,255)) #debugging purposes/shows whats getting added basically
    if calculated:
        cv.putText(roi, "Calculation:", (135 ,190), font, 0.4, (0,255,255))
        cv.putText(roi, str(prosSeq), (135 ,210), font, 0.4, (0,255,255))
        cv.putText(roi, "Result:", (135 ,238), font, 0.4, (25,0,255))
        cv.putText(roi, str(total), (135 ,265), font, 1, (25,0,255))


    cv.imshow("Focus", roi)
    cv.imshow("diffroi", diff)
    cv.imshow("bin", bDiff)
    cv.imshow("Main cam", frame)

    if cv.waitKey(1) & 0xFF == ord("q"):
        break
    
cam.release()
cv.destroyAllWindows()
