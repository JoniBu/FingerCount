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
                    hand = max(contours, key = lambda x: cv.contourArea(x))
                    handArea = cv.contourArea(hand)
                    if handArea < 9000:
                        return("fist")
                    if handArea < 11000:
                        return("palm")
                else:
                    return(str(cnt))

