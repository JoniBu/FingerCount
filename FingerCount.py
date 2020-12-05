from cv2 import cv2 as cv
from detectGesture import detectGesture
import calculator
import util
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


delay = 120
history = []
gestureSeq = []
mostCommon = ""

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
            cv.putText(roi, str(gesture), (5, 25), cv.FONT_HERSHEY_SIMPLEX, 1, (0,255,255))
        else:
            cv.putText(roi, "Unrecognized", (5, 25), cv.FONT_HERSHEY_SIMPLEX, 1, (28,28,212))


        if gesture != None:
            history.append(gesture)
            if len(history) >= delay:
                mostCommon = max(set(history), key = history.count)
                history.clear()
                if len(gestureSeq) >= 2 and (util.isValid(gestureSeq[-2], gestureSeq[-1], mostCommon)):
                    gestureSeq.append(mostCommon)
                elif not gestureSeq and isinstance(mostCommon, int):
                    gestureSeq.append(mostCommon)
                elif len(gestureSeq) == 1 and isinstance(gestureSeq[0], int) and isinstance(mostCommon, str):
                    gestureSeq.append(mostCommon)
                else:
                    cv.putText(roi, "Invalid sequence", (5, 265), cv.FONT_HERSHEY_SIMPLEX, 1, (28,28,212))
                #TODO move above/skip passing "palm" to calculator
                #TODO validation for previous 
                if gestureSeq and mostCommon == "rock": #TODO move above/skip passing "palm" to calculator
                    prosSeq = calculator.createSeq(gestureSeq)
                    print(prosSeq)
                    total = calculator.calculateTotal(prosSeq)
                    # TODO fix these
                    # cv.putText(roi, ("Calculation sequence ", str(prosSeq)), (5, 265), cv.FONT_HERSHEY_SIMPLEX, 1, (255,0,0))
                    # cv.putText(roi, ("Total sum: " , str(total)), (5, 265), cv.FONT_HERSHEY_SIMPLEX, 1, (255,0,0))
            cv.putText(roi, str(mostCommon), (5, 265), cv.FONT_HERSHEY_SIMPLEX, 1, (0,255,255)) #debugging purposes


    cv.imshow("Focus", roi)
    cv.imshow("diffroi", diff)
    cv.imshow("bin", bDiff)
    cv.imshow("Main cam", frame)

    if cv.waitKey(1) & 0xFF == ord("q"):
        break
    
cam.release()
cv.destroyAllWindows()
