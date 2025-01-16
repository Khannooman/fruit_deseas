yolo5s - requirements.txt 
pip install -r yolo5s/reuirements.txt
dataset -train, val
python train.py --img 640 --batch 16 --epochs 50 --data dataset.yaml --weights yolov5s.pt --device 0
python train.py --img 640 --batch 16 --epochs 50 --data dataset.yaml --weights yolov5s.pt --device 0
