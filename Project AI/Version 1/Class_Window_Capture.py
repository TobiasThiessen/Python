import numpy as np
import cv2 as cv                    # https://docs.opencv.org/4.5.5/
from time import time
import win32gui                     # https://github.com/wuxc/pywin32doc/blob/master/md/win32gui.md
import win32ui                      # https://github.com/wuxc/pywin32doc/blob/master/md/win32ui.md
import win32process                 # https://github.com/wuxc/pywin32doc/blob/master/md/win32process.md
import win32con
import PIL.ImageGrab                # https://pillow.readthedocs.io/en/stable/reference/index.html

class Window_Capture:
    
    hwnd = None
    hwnd_rect = None
    hwnd_desktop = False
    draw_FPS = True
    draw_Mouse = True
    FPS = [0]
    Loop_Time = time()
    
    # Class Constructor that is executed whenever we create new objects of this class.
    def __init__(self, window_name):                                                   
        
        # NOTE # Finds window with given name, and sends it to the top (other programs cannot overlay)
        # NOTE # Window MUST be on primary screen, otherwise the view returns nothing
        # NOTE # Can only capture primary screen if it defaults to desktop capture
        self.hwnd = win32gui.FindWindow(None, window_name)
        if self.hwnd:
            win32gui.SetWindowPos(self.hwnd, win32con.HWND_TOPMOST, 0, 0, 0, 0, win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)     
        
        if not self.hwnd:
            self.hwnd = win32gui.GetDesktopWindow()
            self.hwnd_desktop = True

    def Window_Capturer(self):
        
        self.Loop_Time = time()
        
        # NOTE # If Window is found, it will cut off the border for a cleaner look
        if self.hwnd_desktop == False:
            self.hwnd_rect = win32gui.GetWindowRect(self.hwnd)
            x, y, w, h = self.hwnd_rect
            self.hwnd_rect = x + 8, y + 30, w - 8, h - 8
            Screenshot = PIL.ImageGrab.grab(self.hwnd_rect)
            Screenshot = np.ascontiguousarray(Screenshot)
            Screenshot = Screenshot[:, :, ::-1].copy()
        
        # NOTE # If Window is not found, captures desktop and resizes image to 1/4th the size for easier handling
        if self.hwnd_desktop == True:
            self.hwnd_rect = win32gui.GetWindowRect(self.hwnd)
            x, y, w, h = self.hwnd_rect
            Screenshot = PIL.ImageGrab.grab(self.hwnd_rect)
            Screenshot = np.ascontiguousarray(Screenshot)
            Screenshot = Screenshot[:, :, ::-1].copy()
            Screenshot = cv.resize(Screenshot, ((w // 2), (h // 2)))
        
        # NOTE # Will draw mouse a red circle if it is in window / primary desktop - weird limitation of PIL.ImageGrab.grab makes it so it won't capture mouse in picture
        if self.draw_Mouse == True:
            MouseXY = win32gui.GetCursorPos()
            DrawColor = (0, 0, 255)
            DrawXY = (9999, 9999)
            
            if self.hwnd_desktop == False:
                x, y, w, h = self.hwnd_rect
                WindowTopLeft, WindowBotRight = (x, y), (x + w, y + h)
                
                if MouseXY > WindowTopLeft and MouseXY < WindowBotRight:
                    DrawXY = tuple(map(lambda i, j: i - j, MouseXY, WindowTopLeft))
                
            if self.hwnd_desktop == True:
                DrawXY = tuple(map(lambda i, j: i // j, MouseXY, (2, 2)))
                
            
            Screenshot = cv.circle(Screenshot, DrawXY, 5, DrawColor, -1)
        
        # NOTE # Will draw the FPS in the top left corner of the image
        if self.draw_FPS == True:
            self.FPSText = str(round(sum(self.FPS) / len(self.FPS)))
            Screenshot = cv.putText(Screenshot, self.FPSText, (0, 30), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv.FILLED)
            self.FPS.insert(0, 1 / (time() - self.Loop_Time))
            self.FPS = self.FPS[:30]
            return Screenshot
        
        if self.draw_FPS == False:
            return Screenshot