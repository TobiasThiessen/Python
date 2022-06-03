# Class_Window_Overlay.py
Flowchart:
> Class_Window_Overlay |

## __init__(self):
Sets the following variables for the class
```
Draw FPS: True / False
Draw Mouse: True / False
```
1. Draw FPS: if True, will draw FPS on the TOP LEFT of the image
2. Draw Mouse: if True, will capture mouse location and draw a RED DOT accordingly

## Window_Overlay(self, hwnd_desktop, Screenshot):
```
return Screenshot
```
1. Screenshot: Primarily a MAT or NBArray object, made to work with opencv imshow
Called by:
- Class_Window_Capture.Window_Capture(self)
