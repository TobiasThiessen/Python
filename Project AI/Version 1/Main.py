import cv2 as cv                    # https://docs.opencv.org/4.5.5/
from Class_Window_Capture import Window_Capture
A = "Vampire Survivors"
B = "gjghjahajhaht"
WinCap = Window_Capture(B)

while(True):
    
    Screenshot = WinCap.Window_Capturer()
    cv.imshow('AI Vision', Screenshot)
    
    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break