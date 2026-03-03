from ultralytics import YOLO

model = YOLO("runs/detect/train/weights/best.pt")

results = model.predict("leaf_photo.jpg", conf=0.5) # ใส่ภาพตรงนี้ 

results[0].show()
