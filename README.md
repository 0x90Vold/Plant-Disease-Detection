<div align="center">

<br>

```
██████╗ ██╗      █████╗ ███╗   ██╗████████╗    █████╗ ██╗
██╔══██╗██║     ██╔══██╗████╗  ██║╚══██╔══╝   ██╔══██╗██║
██████╔╝██║     ███████║██╔██╗ ██║   ██║      ███████║██║
██╔═══╝ ██║     ██╔══██║██║╚██╗██║   ██║      ██╔══██║██║
██║     ███████╗██║  ██║██║ ╚████║   ██║      ██║  ██║██║
╚═╝     ╚══════╝╚═╝  ╚═╝╚═╝  ╚═══╝   ╚═╝      ╚═╝  ╚═╝╚═╝
```

# 🌿 ระบบตรวจจับโรคพืชด้วย AI

### *ปกป้องพืชผลของคุณด้วยพลัง Computer Vision*

<br>

[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![YOLOv8](https://img.shields.io/badge/YOLOv8-Ultralytics-00D2FF?style=for-the-badge&logo=yolo&logoColor=white)](https://ultralytics.com)
[![mAP50](https://img.shields.io/badge/mAP50-91.67%25-4CAF50?style=for-the-badge&logo=checkmarx&logoColor=white)]()
[![Diseases](https://img.shields.io/badge/โรคพืช-12_ชนิด-FF6B6B?style=for-the-badge&logo=leaf&logoColor=white)]()
[![Dataset](https://img.shields.io/badge/Dataset-5%2C493_รูป-FFA726?style=for-the-badge&logo=database&logoColor=white)]()
[![License](https://img.shields.io/badge/License-CC_BY_4.0-lightgrey?style=for-the-badge)](https://creativecommons.org/licenses/by/4.0/)

<br>

> **ตรวจจับโรคพืชใน 3 พืชหลัก — ถั่ว 🫘 · สตรอเบอรี่ 🍓 · มะเขือเทศ 🍅**
> ด้วยความแม่นยำระดับ 91.67% ในเพียง **7 บรรทัดโค้ด**

<br>

</div>

---

## ⚡ เริ่มต้นใน 60 วินาที

```bash
# 1. ติดตั้ง dependencies
pip install ultralytics

# 2. วางรูปภาพใบพืชของคุณในชื่อ leaf_photo.jpg แล้วรัน
python main.py
```

**หรือรันโดยตรงในโค้ด Python:**

```python
from ultralytics import YOLO                                    # 1. โหลด Framework

model = YOLO("runs/detect/train/weights/best.pt")              # 2. โหลดโมเดล AI

results = model.predict("leaf_photo.jpg", conf=0.5)            # 3. ตรวจจับโรค

results[0].show()                                               # 4. แสดงผลลัพธ์
```

> 💡 **เพียงเท่านี้!** ระบบจะวิเคราะห์รูปภาพและแสดง bounding box พร้อมชื่อโรคและค่าความมั่นใจโดยอัตโนมัติ

---

## 📊 ประสิทธิภาพของโมเดล

<div align="center">

| Metric | Score | ความหมาย |
|:------:|:-----:|:---------|
| 🎯 **mAP50** | **91.67%** | ความแม่นยำหลักในการตรวจจับ |
| ✅ **Precision** | **91.85%** | สัดส่วนการตรวจจับที่ถูกต้อง (ไม่แจ้งเตือนเกินจริง) |
| 🔍 **Recall** | **86.78%** | สัดส่วนการตรวจพบโรคจริงทั้งหมด |
| 📐 **mAP50-95** | **77.15%** | ความแม่นยำรวมทุก IoU Threshold |

</div>

```
Precision ████████████████████████░  91.85%
Recall    ████████████████████░░░░░  86.78%
mAP50     █████████████████████████  91.67%
mAP50-95  ███████████████████░░░░░░  77.15%
```

> 🏋️ **ฝึกฝนด้วยภาพ 5,493 รูป · 100 Epochs · YOLOv8 Nano · ความละเอียด 640×640**

<details>
<summary><b>📈 ดูกราฟผลลัพธ์การฝึกฝน</b></summary>

<br>

<div align="center">

**Training Results Overview**

<img src="runs/detect/train/results.png" width="800" alt="Training Results">

---

**Confusion Matrix**

<img src="runs/detect/train/confusion_matrix.png" width="600" alt="Confusion Matrix">

---

**Normalized Confusion Matrix**

<img src="runs/detect/train/confusion_matrix_normalized.png" width="600" alt="Normalized Confusion Matrix">

---

**Precision-Recall Curve**

<img src="runs/detect/train/BoxPR_curve.png" width="600" alt="PR Curve">

---

**F1-Score Curve**

<img src="runs/detect/train/BoxF1_curve.png" width="600" alt="F1 Curve">

</div>

</details>

<details>
<summary><b>🖼️ ดูตัวอย่าง Prediction vs Ground Truth</b></summary>

<br>

<div align="center">

| 🏷️ Ground Truth | 🤖 Prediction |
|:---:|:---:|
| <img src="runs/detect/train/val_batch0_labels.jpg" width="380"> | <img src="runs/detect/train/val_batch0_pred.jpg" width="380"> |
| <img src="runs/detect/train/val_batch1_labels.jpg" width="380"> | <img src="runs/detect/train/val_batch1_pred.jpg" width="380"> |
| <img src="runs/detect/train/val_batch2_labels.jpg" width="380"> | <img src="runs/detect/train/val_batch2_pred.jpg" width="380"> |

</div>

</details>

---

## 🦠 โรคพืชที่รองรับ (12 ชนิด)

<div align="center">

### 🫘 ถั่ว — 2 โรค

</div>

| # | ชื่อโรค (ไทย) | ชื่อโรค (อังกฤษ) |
|:-:|:---|:---|
| 1 | โรคใบจุดเหลี่ยม | Angular Leaf Spot |
| 2 | โรคสนิม | Rust |

<div align="center">

### 🍓 สตรอเบอรี่ — 7 โรค

</div>

| # | ชื่อโรค (ไทย) | ชื่อโรค (อังกฤษ) |
|:-:|:---|:---|
| 3 | โรคใบจุดเหลี่ยม | Angular Leaf Spot |
| 4 | โรคเน่าผลแอนแทรคโนส | Anthracnose Fruit Rot |
| 5 | โรคดอกไหม้ | Blossom Blight |
| 6 | โรคเทาราแกรย์โมลด์ | Gray Mold |
| 7 | โรคใบจุด | Leaf Spot |
| 8 | โรคราแป้งผล | Powdery Mildew Fruit |
| 9 | โรคราแป้งใบ | Powdery Mildew Leaf |

<div align="center">

### 🍅 มะเขือเทศ — 3 โรค

</div>

| # | ชื่อโรค (ไทย) | ชื่อโรค (อังกฤษ) |
|:-:|:---|:---|
| 10 | โรคใบไหม้ | Blight |
| 11 | โรคราใบ | Leaf Mold |
| 12 | โรคไรแดง | Spider Mites |

---

## 🛠️ ข้อมูลทางเทคนิค

<div align="center">

| Component | Detail |
|:---------:|:------:|
| 🤖 **โมเดล** | YOLOv8 Nano (Ultralytics) |
| 🖼️ **ความละเอียดอินพุต** | 640 × 640 pixels |
| 📦 **ขนาดชุดข้อมูล** | 5,493 รูปภาพที่มีการติดป้าย |
| 🔁 **Epochs** | 100 |
| 🏷️ **จำนวนคลาส** | 12 ชนิดโรค |
| 📋 **Format** | YOLO (.pt weights) |

</div>

### 📁 โครงสร้างไฟล์

```
plant-ai/
├── 📄 main.py                          # ไฟล์หลักสำหรับรัน prediction
├── 🍃 leaf_photo.jpg                   # ใส่รูปภาพของคุณตรงนี้
└── 📂 runs/
    └── 📂 detect/
        └── 📂 train/
            ├── 📂 weights/
            │   └── 🧠 best.pt          # โมเดล AI ที่ฝึกฝนแล้ว ⭐
            ├── 📊 results.png
            ├── 📊 confusion_matrix.png
            └── 📊 BoxPR_curve.png
```

---

## 📚 แหล่งที่มา & เครดิต

โปรเจกต์นี้สร้างขึ้นโดยใช้:

- 📦 **ชุดข้อมูล** — [Roboflow Universe: Detecting Diseases Dataset v6](https://universe.roboflow.com/artificial-intelligence-82oex/detecting-diseases/dataset/6) *(CC BY 4.0)*
- 🤖 **AI Framework** — [Ultralytics YOLOv8](https://github.com/ultralytics/ultralytics)

---


</div>
