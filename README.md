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
  * automatic focusing turned off.


## TODO
### Overall
* More gestures
* Default hand position, add indicators

### Gestures:
* `0-5 numbers` (0 as "ok"-sign or similar)
* fist for `COMBINE` gesture, e.g. 3+5 = 8 - parsed with some small interval 3s, or something
* something as `+` & `-` gestures
* something as `/` & `*` gestures
* `NEXT` gesture, e.g. 3 -> "next" -> 6 = 36
* something as `CALCULATE` gesture
* `RESET` and `REWIND` gestures