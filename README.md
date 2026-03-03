# ระบบตรวจจับโรคพืชด้วย AI

![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![YOLOv26n](https://img.shields.io/badge/YOLOv26n-Ultralytics-00D2FF?style=for-the-badge)
![mAP50](https://img.shields.io/badge/mAP50-91.67%25-4CAF50?style=for-the-badge)
![Diseases](https://img.shields.io/badge/Diseases-12_Types-FF6B6B?style=for-the-badge)

ตรวจจับโรคพืช 12 ชนิดในถั่ว สตรอเบอรี่ และมะเขือเทศ ด้วยความแม่นยำ 91.67%

---

## เริ่มต้นใช้งาน

```bash
pip install ultralytics
python main.py
```

```python
from ultralytics import YOLO

model = YOLO("runs/detect/train/weights/best.pt")
results = model.predict("leaf_photo.jpg", conf=0.5)
results[0].show()
```

---

## ประสิทธิภาพ

| Metric | Score |
|--------|-------|
| mAP50 | 91.67% |
| Precision | 91.85% |
| Recall | 86.78% |
| mAP50-95 | 77.15% |

ฝึกด้วยภาพ 5,493 รูป · 100 Epochs · YOLOv26n · 640×640px

<details>
<summary>กราฟผลลัพธ์</summary>

<img src="runs/detect/train/results.png" width="800">
<img src="runs/detect/train/confusion_matrix_normalized.png" width="600">
<img src="runs/detect/train/BoxPR_curve.png" width="600">

</details>

<details>
<summary>Prediction vs Ground Truth</summary>

| Ground Truth | Prediction |
|:---:|:---:|
| <img src="runs/detect/train/val_batch0_labels.jpg" width="380"> | <img src="runs/detect/train/val_batch0_pred.jpg" width="380"> |
| <img src="runs/detect/train/val_batch1_labels.jpg" width="380"> | <img src="runs/detect/train/val_batch1_pred.jpg" width="380"> |

</details>

---

## โรคที่รองรับ (12 ชนิด)

**ถั่ว (2):** Angular Leaf Spot · Rust

**สตรอเบอรี่ (7):** Angular Leaf Spot · Anthracnose Fruit Rot · Blossom Blight · Gray Mold · Leaf Spot · Powdery Mildew Fruit · Powdery Mildew Leaf

**มะเขือเทศ (3):** Blight · Leaf Mold · Spider Mites

---

## แหล่งที่มา

- Dataset: [Roboflow Universe](https://universe.roboflow.com/artificial-intelligence-82oex/detecting-diseases/dataset/6) (CC BY 4.0)
- Framework: [Ultralytics YOLOv8](https://github.com/ultralytics/ultralytics)
