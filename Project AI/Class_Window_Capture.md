# Class_Window_Capture.py
##### Class Flowchart:
> Class_Window_Capture (ON/OFF) >>> Class_Window_Overlay |

## __init__(self):
Sets the following variables for the class
```
hwnd = win32gui.FindWindow(None, selected_hwnd)
hwnd_overlay = True
hwnd_resize = True
```
> hwnd_overlay: if enabled, Class_Window_Overlay will be constructed

## Window_Capture(self):
Screenshots desired window or primary screen.
```
self.hwnd_rect = win32gui.GetWindowRect(self.hwnd)
Screenshot = PIL.ImageGrab.grab(self.hwnd_rect)
Screenshot = np.ascontiguousarray(Screenshot)
Screenshot = Screenshot[:, :, ::-1].copy()
return Screenshot
```
> Screenshot: is a MAT or NBArray variable usable by openCV
##### Called by:
- Class_Window_Search.FIND(self, Threshold, State)
