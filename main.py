from ultralytics import YOLO
import os

checkpoint_path = "runs/detect/train/weights/last.pt"

if os.path.exists(checkpoint_path):
    model = YOLO(checkpoint_path)
    train_results = model.train(resume=True)
else:
    model = YOLO("yolo26n.pt")
    train_results = model.train(
        data="data.yaml",
        epochs=100,
        imgsz=640,
        device="0",
        workers=0
    )

metrics = model.val()
