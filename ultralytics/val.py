import warnings
warnings.filterwarnings('ignore')
from ultralytics import RTDETR

if __name__ == '__main__':
    model = RTDETR('weights/best.pt')
    model.val(data='ultralytics/cfg/dataset/VisDone.yaml',
              split='test',
              imgsz=640,
              batch=4,
              save_json=True, 
              project='runs/val',
              name='GSConv-rtdetr',
              )
