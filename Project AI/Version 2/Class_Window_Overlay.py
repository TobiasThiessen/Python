from time import time
import cv2 as cv                    # https://docs.opencv.org/4.5.5/
import win32gui                     # https://github.com/wuxc/pywin32doc/blob/master/md/win32gui.md
import tkinter as tk                # https://docs.python.org/3/library/tk.html
from tkinter.messagebox import askyesno

ROOT = tk.Tk()
ROOT.withdraw()

class Window_Overlay:
    
    draw_overlay = False
    draw_FPS = False
    draw_Mouse = False
    FPS = [0]
    Loop_Time = time()
    
    # NOTE # Class Constructor that is executed whenever we create new objects of this class.
    def __init__(self):
        
        UserInput = askyesno("Project AI", "Enable Overlay?")
        if UserInput == True:
            self.draw_overlay = True
            
            UserInput = askyesno("Project AI", "Draw FPS?")
            if UserInput == True:
                self.draw_FPS = True
                
            UserInput = askyesno("Project AI", "Draw Mouse?")
            if UserInput == True:
                self.draw_Mouse = True
                
            if self.draw_FPS == True:
                self.Loop_Time = time()
                
    # NOTE # Takes the screenshot from Class_Window_Capture and draws various overlay elements.
    # NOTE # hwnd_desktop: A switch enabling the overlay
    # NOTE # hwnd: The name of the window, a string
    # NOTE # Screenshot: Image taken by PILLOW and modified by numpy
    def Window_Overlay(self, hwnd_desktop, hwnd, Screenshot):  
    
        if self.draw_overlay == False:
            return Screenshot
        
        # NOTE # Will draw the Mouse as a red dot on the image as PILLOW cannot capture the mouse in screenshots
        if self.draw_Mouse == True:
            MouseXY = win32gui.GetCursorPos()
            DrawColor = (0, 0, 255)
            DrawXY = (9999, 9999)
            
            
            if hwnd_desktop == False:
                self.hwnd_rect = win32gui.GetWindowRect(hwnd)
                x, y, w, h = self.hwnd_rect
                x, y, w, h = x + 8, y + 30, w - 8, h - 8
                WindowTopLeft, WindowBotRight = (x, y), (x + w, y + h)
                
                if MouseXY > WindowTopLeft and MouseXY < WindowBotRight:
                    DrawXY = tuple(map(lambda i, j: i - j, MouseXY, WindowTopLeft))
                
            # NOTE # As the image is being resized in Class_Window_Capture if it is the desktop being captured
            # NOTE # We must reduce the values of the MouseXY location so they are drawn in the right place
            if hwnd_desktop == True:
                DrawXY = MouseXY
                #DrawXY = tuple(map(lambda i, j: i // j, MouseXY, (2, 2)))
                
            
            Screenshot = cv.circle(Screenshot, DrawXY, 5, DrawColor, -1)
        
        # NOTE # Will draw the FPS in the top left corner of the image
        if self.draw_FPS == True:
            
            FPSText = str(round(sum(self.FPS) / len(self.FPS)))
            self.FPS.insert(0, 1 / (time() - self.Loop_Time))
            self.FPS = self.FPS[:30]
            self.Loop_Time = time()
            Screenshot = cv.putText(Screenshot, FPSText, (0, 30), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv.FILLED)
            
        return Screenshot