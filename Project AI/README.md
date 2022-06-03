# Project AI

## Version 1
Using openCV, win32gui and PILLOW to screenshot any window or the primary desktop.
Draws mouse location on the screenshots (red dot) and FPS if enabled in the code.

## Version 2
Moved the overlay into its own class file, and using tkinter made prompts to help setup when running Main.py

## Version 3
N/A

#
# Function Documention / Index
## Main.py
```
Flowchart:
Main >>> Class_Game_VampireSurvivors >>> Class_Window_Search >>> Class_Window_Capture >>> Class_Window_Overlay
```

## Class_Window_Capture.py
```
Flowchart:
Class_Window_Capture (ON/OFF) >>> Class_Window_Overlay
```
### __init__(self):
Builds a window with tkINTER and prompts user for desired settings. (Such as Overlay)

### Window_Capture(self)
Screenshots desired window or primary screen.
> return Screenshot
[Used by: Class_Window_Search.FIND(self, Threshold, State]

## Class_Window_Overlay.py
