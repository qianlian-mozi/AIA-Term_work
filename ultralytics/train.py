import warnings
warnings.filterwarnings('ignore')
from ultralytics import RTDETR

if __name__ == '__main__':
    model = RTDETR('ultralytics/cfg/model/rtdetr-slimneck.yaml')
    # model.load('') # loading pretrain weights
    model.train(data='ultralytics/cfg/dataset/VisDone.yaml',
                cache=False,
                imgsz=640,
                epochs=100,
                batch=4,
                workers=4,
                device='0',
                # resume='', # last.pt path
                project='runs/train',
                name='GSConv-rtdetr',
                )
    # ultralytics\cfg\models\rt-detr\