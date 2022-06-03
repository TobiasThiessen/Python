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
Flowchart:
> Main >>> Class_Game_VampireSurvivors >>> Class_Window_Search >>> Class_Window_Capture >>> Class_Window_Overlay |

## Class_Window_Capture.py
Flowchart:
> Class_Window_Capture (ON/OFF) >>> Class_Window_Overlay |

### __init__(self):
Sets the following variables for the class
```
hwnd = String
Overlay = True / False
hwnd_resize = True / False
```
1. hwnd: window handle string used to detect desired window in Window_Capture
2. Overlay: if True, will enable screenshot manipulation that draws certain features.
3. hwnd_resize: if True, will resize the screenshot to always be 1/4th the size of the primary monitor 

### Window_Capture(self):
Screenshots desired window or primary screen.
```
return Screenshot
```
1. Screenshot: Primarily a MAT or NBArray object, made to work with opencv imshow
Called by:
- Class_Window_Search.FIND(self, Threshold, State)

## Class_Window_Overlay.py
Flowchart:
> Class_Window_Overlay |

### __init__(self):
Sets the following variables for the class
```
Draw FPS: True / False
Draw Mouse: True / False
```
1. Draw FPS: if True, will draw FPS on the TOP LEFT of the image
2. Draw Mouse: if True, will capture mouse location and draw a RED DOT accordingly

### Window_Overlay(self, hwnd_desktop, Screenshot):
```
return Screenshot
```
1. Screenshot: Primarily a MAT or NBArray object, made to work with opencv imshow
Called by:
- Class_Window_Capture.Window_Capture(self)
