import math
from cv2 import cv2 as cv


def detectGesture(contours, res, hull):
    cnt = 0
    if len(hull) > 3:
            defects = cv.convexityDefects(res, hull)
            if type(defects) != type(None):  # avoid crashing.   (BUG not found)
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
                if cnt == 0:
                    hhArea, ratio = calculateAreas(contours)
                    if ratio > 0.9: #extra verification
                        if  hhArea < 17500:
                            return("fist")
                        if  hhArea > 17500:
                            return("palm")
                    if ratio < 0.8 and hhArea > 22000:
                        return("call")
                    else:
                        return(cnt+1)
                elif cnt == 1:
                    hhArea, ratio = calculateAreas(contours)
                    if ratio > 0.65 and hhArea > 23000:
                        return("vulcan")
                    return(cnt+1)
                elif cnt == 2:
                    hhArea, ratio = calculateAreas(contours)
                    if ratio < 0.7 and hhArea > 29000:
                        return("rock")
                    return(cnt+1)
                else:
                    return(cnt+1)

def calculateAreas(contours):
    hand = max(contours, key = lambda x: cv.contourArea(x))
    handArea = cv.contourArea(hand)
    handHull = cv.convexHull(hand)
    hhArea = cv.contourArea(handHull)
    ratio = handArea / hhArea
    return hhArea, ratio
    #return handArea, hhArea, ratio - hand area not used currently, so decided not to return it
    

