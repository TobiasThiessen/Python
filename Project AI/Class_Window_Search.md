# Class_Window_Search
##### Class Flowchart:
> Class_Window_Search >>> Class_Window_Capture |

## __init__(self, NeedleImage_Path):
Requires file path to Needle Image
Sets the following variables for the class
```
NeedleImage = cv.imread(NeedleImage_Path, cv.IMREAD_UNCHANGED)
NeedleImage_W = NeedleImage.shape[1]
NeedleImage_H = NeedleImage.shape[0]
Method = TM_SQDIFF, TM_SQDIFF_NORMED, TM_CCORR, TM_CCORR_NORMED, TM_CCOEFF, TM_CCOEFF_NORMED
```
> NeedleImage: is a MAT variable made and usable by openCV

## FIND(self, threshold = 0.5, State = 1):
Threshold is used to determine accuracy of the function, 1 requires 1:1 HaystackImage:NeedleImage Pixels 
```
HaystackImage = Class_Window_Capture.Window_Capture()
cv.matchTemplate(HaystackImage, self.NeedleImage, self.Method)
if state == 1:
	return False / True
if state == 2: 
	return HaystackImage
```
> HaystackImage is a MAT or NBArray variable usable by openCV
