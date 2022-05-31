import cv2 as cv                    # https://docs.opencv.org/4.5.5/
from Class_Window_Capture import Window_Capture

WinCap = Window_Capture()

while(True):
    
    Screenshot = WinCap.Window_Capture()
    cv.imshow('AI Vision', Screenshot)
    
    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break