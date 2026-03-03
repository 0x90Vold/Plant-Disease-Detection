# ระบบตรวจจับโรคพืชด้วย AI

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8+-blue?style=for-the-badge&logo=python)
![YOLO](https://img.shields.io/badge/YOLOv8-Ultralytics-00D2FF?style=for-the-badge)
![Accuracy](https://img.shields.io/badge/Accuracy-91.67%25-4CAF50?style=for-the-badge)
![Diseases](https://img.shields.io/badge/Diseases-12_Types-FF6B6B?style=for-the-badge)

**ตรวจจับโรคพืช 12 ชนิด ด้วย AI ในเพียง 7 บรรทัดโค้ด**

*ระบบ AI สำหรับการตรวจจับโรคในพืชถั่ว สตรอเบอรี่ และมะเขือเทศ*

</div>

## เริ่มต้นใช้งาน

```bash
# ติดตั้ง dependencies
pip install ultralytics

# วางรูปภาพพืชของคุณเป็นชื่อ "leaf_photo.jpg" แล้วรันคำสั่ง:
python main.py
```

**หรือใช้โค้ดนี้โดยตรง:**
```python
from ultralytics import YOLO

model = YOLO("runs/detect/train/weights/best.pt")
results = model.predict("leaf_photo.jpg", conf=0.5)
results[0].show()
```

<br>

---

<br>

## ประสิทธิภาพของโมเดล

| Metric | Score | Description |
|--------|-------|-------------|
| **mAP50** | 91.67% | ความแม่นยำหลัก |
| **Precision** | 91.85% | อัตราการตรวจจับที่ถูกต้อง |
| **Recall** | 86.78% | อัตราการตรวจจับโรค |
| **mAP50-95** | 77.15% | ความแม่นยำโดยรวม |

**ฝึกฝนด้วยภาพ 5,493 รูป • 100 epochs • YOLOv8 Nano**

<br>

<details>
<summary><b>กราฟผลลัพธ์ (คลิกเพื่อดู)</b></summary>

<br>

<div align="center">

**ผลลัพธ์การฝึกฝน**

<img src="runs/detect/train/results.png" width="800">

<br>

**เมทริกซ์ความสับสน**

<img src="runs/detect/train/confusion_matrix.png" width="600">

<br>

**เมทริกซ์ความสับสน (ปรับมาตรฐาน)**

<img src="runs/detect/train/confusion_matrix_normalized.png" width="600">

<br>

**กราฟ PR Curve**

<img src="runs/detect/train/BoxPR_curve.png" width="600">

<br>

**กราฟ F1 Curve**

<img src="runs/detect/train/BoxF1_curve.png" width="600">

</div>

</details>

<br>

<details>
<summary><b>ตัวอย่าง Prediction vs Ground Truth (คลิกเพื่อดู)</b></summary>

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

## ตัวอย่างโค้ด

<div align="center">

**โค้ดการตรวจจับทั้งหมดใช้เพียง 7 บรรทัด!**

```python
from ultralytics import YOLO

model = YOLO("runs/detect/train/weights/best.pt")

results = model.predict("leaf_photo.jpg", conf=0.5) # ใส่ภาพตรงนี้ 

results[0].show()
```

<br>

<table>
<tr>
<td align="center">
  <img src="https://img.shields.io/badge/1-Import_YOLO-FF6B6B?style=for-the-badge&labelColor=1a1a1a" alt="Step 1"/>
  <br><sub>โหลด Framework</sub>
</td>
<td align="center">
  <img src="https://img.shields.io/badge/2-Load_Model-4ECDC4?style=for-the-badge&labelColor=1a1a1a" alt="Step 2"/>
  <br><sub>AI พร้อมใช้งาน</sub>
</td>
<td align="center">
  <img src="https://img.shields.io/badge/3-Predict-45B7D1?style=for-the-badge&labelColor=1a1a1a" alt="Step 3"/>
  <br><sub>ตรวจจับโรค</sub>
</td>
<td align="center">
  <img src="https://img.shields.io/badge/4-Show-96CEB4?style=for-the-badge&labelColor=1a1a1a" alt="Step 4"/>
  <br><sub>ดูผลลัพธ์</sub>
</td>
</tr>
</table>

</div>

<br>

---

<br>

## โรคพืชที่รองรับ (12 ชนิด)

### โรคในถั่ว (2 ชนิด)
- โรคใบจุดเหลี่ยม (Angular Leaf Spot)
- โรคสนิม (Rust)

### โรคในสตรอเบอรี่ (7 ชนิด)
- โรคใบจุดเหลี่ยม (Angular Leaf Spot)
- โรคเน่าผลแอนแทรคโนส (Anthracnose Fruit Rot)
- โรคดอกไหม้ (Blossom Blight)
- โรคเทาราแกรย์โมลด์ (Gray Mold)
- โรคใบจุด (Leaf Spot)
- โรคราแป้งผล (Powdery Mildew Fruit)
- โรคราแป้งใบ (Powdery Mildew Leaf)

### โรคในมะเขือเทศ (3 ชนิด)
- โรคใบไหม้ (Blight)
- โรคราใบ (Leaf Mold)
- โรคไรแดง (Spider Mites)

<br>

---

<br>

## โครงสร้างโปรเจค

```
Plant-Disease-Detection/
├── main.py                      # สคริปต์ตรวจจับโรค (7 บรรทัด)
├── requirements.txt             # ไลบรารีที่ต้องใช้
├── data.yaml                    # การตั้งค่าชุดข้อมูล
├── yolo26n.pt                   # โมเดลที่ฝึกมาแล้ว
└── runs/detect/train/
    ├── weights/best.pt          # โมเดลที่ดีที่สุด
    ├── results.png              # กราฟผลการฝึก
    └── confusion_matrix.png     # การวิเคราะห์ประสิทธิภาพ
```

## ข้อมูลทางเทคนิค

- **โมเดล**: YOLOv8 Nano (เบาและเร็ว)
- **ชุดข้อมูล**: 5,493 รูปภาพที่มีการติดป้าย
- **ความละเอียด**: 640×640 พิกเซล
- **การฝึก**: 100 epochs
- **จำนวนคลาส**: 12 ชนิดโรค

## แหล่งที่มาของข้อมูล

**สร้างขึ้นด้วย:**
- **ชุดข้อมูล**: [Roboflow Universe](https://universe.roboflow.com/artificial-intelligence-82oex/detecting-diseases/dataset/6) (CC BY 4.0)
- **เฟรมเวิร์ค AI**: [Ultralytics YOLOv8](https://github.com/ultralytics/ultralytics)
