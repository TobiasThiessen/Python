# Custom Model for Object Detection powered by Tensorflow
## Program Prerequisites:
Known to work:
- Python 3.10.4
- CUDA 11.2 
- CudNN 8.1.1
- PIP 22.1.2
- GIT 2.26.1.windows.1
- more

Known to not work:
- CUDA 11.7
- cudNN 8.4.1


CUDA download:  https://developer.nvidia.com/cuda-downloads (may require nvidia dev account (free))
cuDNN download: https://developer.nvidia.com/rdp/cudnn-download (requires nvidia dev account (free))



## Installation / Setup:
#### Step 1: Install prerequisites
Check if CUDA 11.2 is installed by typing in cmd or shell:
> nvcc --version
Check if cuDNN 8.1.1 is installed by reading the following header file:
> NVIDIA GPU Computing Toolkit\CUDA\v11.2\include\cudnn_version.h


#### Step 2: Run "environment_setup.py"
Use whatever method to run the script, i.e. from IDE or CMD.
This should automatically make a virtual environment named "VENV" and install all the necesarry packages from "library_requirements.txt".



### Model Zoo:
https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/tf2_detection_zoo.md

Known to work:
- SSD MobileNet V2 FPNLite 640x640

Known to not work:
- CenterNet Resnet50 V2 512x512
