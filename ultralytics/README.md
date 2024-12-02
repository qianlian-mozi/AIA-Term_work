# How to use the given code to train or test

1. Copy the files provided in this folder and overwrite the corresponding paths of the [official ultralytics repository](https://github.com/ultralytics/ultralytics/tree/v8.0.201). Our code is based on the v8.0.201 version of ultralytics.

`git clone https://github.com/ultralytics/ultralytics.git -b v8.0.201`

2. The method trained and tested on '12 vCPU Intel(R) Xeon(R) Platinum 8352V CPU @ 2.10GHz' and 'one RTX 4090(24GB) GPU'. The vision of pytorch is 1.11.0+cu113 and torchvision is 0.12.0+cu113.

3. If some environment errors occur, install the following packages(If nothing occurs, you may not need them):
```
pip install timm==0.9.8 thop efficientnet_pytorch==0.7.1 einops grad-cam==1.4.8 dill==0.3.6 albumentations==1.3.1 pytorch_wavelets==1.3.0 tidecv
pip install -U openmim
mim install mmengine
mim install "mmcv>=2.0.0"
# For other packges missing, refer to your error message and just pip/conda install them.
```

4. To test the model we provided, check the given `train.py` and `val.py` files, modify the corresponding hyperparameters as you want for you own project and just run them.