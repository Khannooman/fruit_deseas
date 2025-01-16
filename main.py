import torch
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
from ultralytics import YOLO
model = YOLO("yolov5s.pt")
model.to(device)
model.train(data="dataset.yaml", epochs=50, batch=16, imgsz=640, device=0)

