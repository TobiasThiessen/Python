# Class_Window_Overlay.py
##### Class Flowchart:
> Class_Window_Overlay |

## __init__(self):
Sets the following variables for the class
```
draw_FPS = True / False
draw_Mouse = True / False
if draw_FPS:
    Loop_Time = time()
```
> Loop_Time: Used to count the amount of screenshots taken per second, which translates to FPS

## Window_Overlay(self, hwnd_desktop, hwnd, Screenshot):
```
if draw_Mouse:
    MouseXY = win32gui.GetCursorPos()
    if hwnd_desktop:
        DrawXY = MouseXY
    if not hwnd_desktop:
        DrawXY = tuple(map(lambda i, j: i - j, MouseXY, WindowTopLeft))
    Screenshot = cv.circle(Screenshot, DrawXY, 5, DrawColor, -1)
    
if draw_FPS:
    FPSText = str(round(sum(self.FPS) / len(self.FPS)))
    Screenshot = cv.putText(Screenshot, FPSText, (0, 30), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv.FILLED)
    
 return Screenshot
```
> Screenshot: Primarily a MAT or NBArray object, made to work with opencv imshow
##### Called by:
- Class_Window_Capture.Window_Capture(self)
