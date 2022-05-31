import numpy as np
import cv2 as cv                    # https://docs.opencv.org/4.5.5/
from time import time
import win32gui                     # https://github.com/wuxc/pywin32doc/blob/master/md/win32gui.md
import win32con
import PIL.ImageGrab                # https://pillow.readthedocs.io/en/stable/reference/index.html
from Class_Window_Overlay import Window_Overlay
from tkinter.simpledialog import askstring

Overlay = Window_Overlay()

class Window_Capture:
    
    hwnd = None
    hwnd_rect = None
    hwnd_desktop = False
    hwnd_overlay = False
    Screenshot = None
    
    Desktop_X, Desktop_Y, Desktop_W, Desktop_H = win32gui.GetWindowRect(win32gui.GetDesktopWindow())

    # Class Constructor that is executed whenever we create new objects of this class.
    def __init__(self):                                                   
        
        # NOTE # Finds window with given name, and sends it to the top (other programs cannot overlay)
        # NOTE # Window MUST be on primary screen, otherwise the view returns nothing
        # NOTE # Can only capture primary screen if it defaults to desktop capture
        window_name = askstring("Project AI", "Name of Window to Capture? Leave blank for desktop")
        self.hwnd = win32gui.FindWindow(None, window_name)
        if self.hwnd:
            win32gui.SetWindowPos(self.hwnd, win32con.HWND_TOPMOST, 0, 0, 0, 0, win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)
            win32gui.ShowWindow(self.hwnd, win32con.SW_SHOWNORMAL)
        
        if not self.hwnd or window_name == None:
            self.hwnd = win32gui.GetDesktopWindow()
            self.hwnd_desktop = True

    def Window_Capture(self):
        
        #self.Loop_Time = time()
        
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
            #Screenshot = cv.resize(Screenshot, ((w // 2), (h // 2)))

        # NOTE # Draws overlay if enabled on startup
        Screenshot = Overlay.Window_Overlay(self.hwnd_desktop, self.hwnd, Screenshot)
        
        Screenshot_H, Screenshot_W = Screenshot.shape[:2]
        if Screenshot_H > (self.Desktop_H // 2) or Screenshot_W > (self.Desktop_W // 2):
            Screenshot = cv.resize(Screenshot, ((self.Desktop_W // 2), (self.Desktop_H // 2)))
        
        return Screenshot