# Project AI

## Version 1
Using openCV, win32gui and PILLOW to screenshot any window or the primary desktop.
Draws mouse location on the screenshots (red dot) and FPS if enabled in the code.

## Version 2
Moved the overlay into its own class file, and using tkinter made prompts to help setup when running Main.py

## Version 3
N/A


# Function Documention / Index
## Main.py
```
Flowchart:
Main --] Game_VampireSurvivors --] Window_Search --] Window_Capture --] Window_Overlay
```

## Class_Window_Capture.py
```
Flowchart:
Window_Capture (ON/OFF) --] Window_Overlay
```
### __init__(self):
Builds a window with tkINTER and prompts user for desired settings. (Such as Overlay)
Used by: Class_Window_Capture.Window_Capture()

### Window_Capture(self)
Screenshots desired window or primary screen.
> Returns Screenshot

## Class_Window_Overlay.py
