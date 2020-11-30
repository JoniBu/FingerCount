import math
from cv2 import cv2 as cv


#source for calculating fingers https://github.com/lzane/Fingers-Detection-using-OpenCV-and-Python
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
                return(str(cnt))
            # else: TODO add support for more gestures, detect palm and fist based on ratio of contours
            #     #if (res != []) and (hull != []):
            #     handContour = max(contours, key = lambda x: cv.contourArea(x))
            #     handArea = cv.contourArea(handContour)
            #     hullArea = cv.contourArea(hull)
            #     print(handArea, hullArea)


            #TODO determine and detect gestures for operations