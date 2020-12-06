# Finger Count

Simple calculator built with OpenCV and Python3 that uses one hand gestures as input for the calculations.

Ran from `FingerCount.py`. Stopped by pressing "q".


## Base idea
* Simple calculator with input parsed from hand gestures.
* Small interval to combine numbers (wait until `COMBINE` sign).


## Prerequisites
* Python3
* OpenCV
* Webcam with;
  * static background,
  * automatic focusing turned off (this is done from code as well).


## TODO
### Overall
* Add gesture/way to add just 1
* More gestures
  * Update gesture list
* Overall code cleanup..
* Folders
* Sample video(s)

### Gestures:
* `1-5` count of fingers
* fist for `COMBINE` gesture, e.g. 3+5 = 8 - parsed with some small interval 3s, or something
* something as `+` & `-` gestures
* something as `/` & `*` gestures
* `NEXT` gesture, e.g. 3 -> "next" -> 6 = 36
* something as `CALCULATE` gesture
* `RESET` and `REWIND` gestures