<div align="center">

# 🌿 Plant Disease Detection

### ตรวจจับโรคพืชแบบ Real-time ด้วย YOLOv26

[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![YOLO](https://img.shields.io/badge/YOLOv26-Ultralytics-00FFFF?style=for-the-badge&logo=yolo&logoColor=white)](https://github.com/ultralytics/ultralytics)
[![Roboflow](https://img.shields.io/badge/Dataset-Roboflow-6706CE?style=for-the-badge&logo=roboflow&logoColor=white)](https://universe.roboflow.com/artificial-intelligence-82oex/detecting-diseases/dataset/6)
[![License](https://img.shields.io/badge/License-CC_BY_4.0-EF9421?style=for-the-badge&logo=creativecommons&logoColor=white)](https://creativecommons.org/licenses/by/4.0/)

<br>

> **ระบุโรคพืชจากภาพถ่าย** — รองรับ ถั่ว 🫘 สตรอว์เบอร์รี 🍓 มะเขือเทศ 🍅  
> ครอบคลุม **12 โรค** • เทรนจาก **~5,500 ภาพ** • แค่รันก็ใช้ได้เลย

</div>

<br>

---

<br>

## 📊 ผลลัพธ์การเทรน

<div align="center">

| Metric | Score |
|:------:|:-----:|
| **mAP50** | `91.67%` |
| **mAP50-95** | `77.15%` |
| **Precision** | `91.85%` |
| **Recall** | `86.78%` |

> 🏆 ผลลัพธ์จากการเทรน **100 epochs** บน **~5,500 ภาพ** ด้วย YOLOv26 Nano

</div>

<br>

<details>
<summary><b>📈 กราฟผลลัพธ์ (คลิกเพื่อดู)</b></summary>

<br>

<div align="center">

**Training Results**

<img src="runs/detect/train/results.png" width="800">

<br>

**Confusion Matrix**

<img src="runs/detect/train/confusion_matrix.png" width="600">

<br>

**Confusion Matrix (Normalized)**

<img src="runs/detect/train/confusion_matrix_normalized.png" width="600">

<br>

**PR Curve**

<img src="runs/detect/train/BoxPR_curve.png" width="600">

<br>

**F1 Curve**

<img src="runs/detect/train/BoxF1_curve.png" width="600">

</div>

</details>

<br>

<details>
<summary><b>🖼️ ตัวอย่าง Prediction vs Ground Truth (คลิกเพื่อดู)</b></summary>

<br>

<div align="center">

| Ground Truth | Prediction |
|:---:|:---:|
| <img src="runs/detect/train/val_batch0_labels.jpg" width="400"> | <img src="runs/detect/train/val_batch0_pred.jpg" width="400"> |
| <img src="runs/detect/train/val_batch1_labels.jpg" width="400"> | <img src="runs/detect/train/val_batch1_pred.jpg" width="400"> |
| <img src="runs/detect/train/val_batch2_labels.jpg" width="400"> | <img src="runs/detect/train/val_batch2_pred.jpg" width="400"> |

</div>

</details>

<br>

---

<br>

## 🚀 Quick Start

```bash
# 1️⃣ ติดตั้ง
pip install ultralytics

# 2️⃣ เทรนโมเดล
python main.py

# 3️⃣ ทำนาย
yolo predict model=runs/detect/train/weights/best.pt source="path/to/image.jpg"
```

<br>

## 🧠 ใช้งานใน Python

```python
from ultralytics import YOLO

# โหลดโมเดลที่เทรนแล้ว
model = YOLO("runs/detect/train/weights/best.pt")

# ทำนายจากภาพ
results = model.predict("leaf_photo.jpg", conf=0.5)

# แสดงผล
results[0].show()
```

<br>

---

<br>

## 🏷️ โรคที่ตรวจจับได้

<table>
<tr>
<td align="center" width="33%">

### 🫘 ถั่ว

| # | โรค |
|:-:|:---|
| 1 | Angular Leaf Spot |
| 2 | Rust |

</td>
<td align="center" width="33%">

### 🍓 สตรอว์เบอร์รี

| # | โรค |
|:-:|:---|
| 1 | Angular Leaf Spot |
| 2 | Anthracnose Fruit Rot |
| 3 | Blossom Blight |
| 4 | Gray Mold |
| 5 | Leaf Spot |
| 6 | Powdery Mildew (Fruit) |
| 7 | Powdery Mildew (Leaf) |

</td>
<td align="center" width="33%">

### 🍅 มะเขือเทศ

| # | โรค |
|:-:|:---|
| 1 | Blight |
| 2 | Leaf Mold |
| 3 | Spider Mites |

</td>
</tr>
</table>

<br>

---

<br>

## 📂 โครงสร้างโปรเจค

```
🌿 Plant-Disease-Detection/
│
├── 📄 main.py              ← สคริปต์เทรน (รองรับ resume อัตโนมัติ)
├── 📄 data.yaml             ← config dataset & class names
├── 🧠 yolo26n.pt            ← pretrained weights (Nano)
│
├── 📁 train/                ← ~2,900 ภาพสำหรับเทรน
├── 📁 valid/                ← ~1,400 ภาพสำหรับ validate
├── 📁 test/                 ← ~1,100 ภาพสำหรับทดสอบ
│
└── 📁 runs/detect/train/    ← ผลลัพธ์การเทรน
     ├── weights/            ← best.pt & last.pt
     ├── results.png         ← กราฟ loss & metrics
     ├── confusion_matrix.png
     └── ...                 ← PR curve, F1 curve, etc.
```

<br>

---

<br>

## ⚙️ Training Config

<div align="center">

| Parameter | Value |
|:---------:|:-----:|
| **Model** | `YOLOv26 Nano` |
| **Epochs** | `100` |
| **Batch Size** | `16` |
| **Image Size** | `640 × 640` |
| **Optimizer** | `Auto (SGD)` |
| **Learning Rate** | `0.01` |
| **Dataset** | `~5,493 images` |
| **Resume** | `✅ Auto-checkpoint` |

</div>

<br>

<details>
<summary><b>💡 หมายเหตุ — main.py รองรับ resume อัตโนมัติ</b></summary>

<br>

ถ้าเทรนค้างอยู่ สคริปต์จะเช็ค checkpoint ที่ `runs/detect/train/weights/last.pt`  
แล้ว **resume ต่อจากจุดที่หยุด** ให้เองเลย ไม่ต้องเทรนใหม่ตั้งแต่ต้น ✌️

</details>

<br>

---

<br>

## 🙏 Credits & Acknowledgements

<div align="center">

|  |  |
|:-:|:-:|
| [![Roboflow](https://img.shields.io/badge/Roboflow-6706CE?style=for-the-badge&logo=roboflow&logoColor=white)](https://roboflow.com) | Dataset จาก [Roboflow Universe](https://universe.roboflow.com/artificial-intelligence-82oex/detecting-diseases/dataset/6) |
| [![Ultralytics](https://img.shields.io/badge/Ultralytics-111F68?style=for-the-badge&logo=yolo&logoColor=white)](https://ultralytics.com) | YOLOv26 Model โดย [Ultralytics](https://github.com/ultralytics/ultralytics) |

</div>

<br>

---

<div align="center">

**⭐ ถ้าโปรเจคนี้มีประโยชน์ กด Star ให้ด้วยนะครับ!**

<sub>Made with 💚 for smarter agriculture</sub>

</div>
