# Class_Window_Capture.py
Flowchart:
> Class_Window_Capture (ON/OFF) >>> Class_Window_Overlay |

## __init__(self):
Sets the following variables for the class
```
hwnd = String
Overlay = True / False
hwnd_resize = True / False
```
1. hwnd: window handle string used to detect desired window in Window_Capture
2. Overlay: if True, will enable screenshot manipulation that draws certain features.
3. hwnd_resize: if True, will resize the screenshot to always be 1/4th the size of the primary monitor 

## Window_Capture(self):
Screenshots desired window or primary screen.
```
return Screenshot
```
1. Screenshot: Primarily a MAT or NBArray object, made to work with opencv imshow
Called by:
- Class_Window_Search.FIND(self, Threshold, State)
