# 🌱 Plant Disease Detection AI

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8+-blue?style=for-the-badge&logo=python)
![YOLO](https://img.shields.io/badge/YOLOv8-Ultralytics-00D2FF?style=for-the-badge)
![Accuracy](https://img.shields.io/badge/Accuracy-91.67%25-4CAF50?style=for-the-badge)
![Diseases](https://img.shields.io/badge/Diseases-12_Types-FF6B6B?style=for-the-badge)

**🚀 ตรวจจับโรคพืช 12 ชนิด ด้วย AI ใน 7 บรรทัดโค้ด**

*AI-Powered Plant Disease Detection for Beans, Strawberries & Tomatoes*

</div>

## ⚡ Quick Start

```bash
# Install requirements
pip install ultralytics

# Place your plant image as "leaf_photo.jpg" then run:
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

## 📊 Model Performance

| Metric | Score | Description |
|--------|-------|-------------|
| **mAP50** | 91.67% | Primary accuracy |
| **Precision** | 91.85% | True positive rate |
| **Recall** | 86.78% | Disease detection rate |
| **mAP50-95** | 77.15% | Overall accuracy |

🏆 **Trained on 5,493 images • 100 epochs • YOLOv8 Nano**

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

## � **Code Example**

<div align="center">

**The entire detection code is just 7 lines!**

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
  <br><sub>Load Framework</sub>
</td>
<td align="center">
  <img src="https://img.shields.io/badge/2-Load_Model-4ECDC4?style=for-the-badge&labelColor=1a1a1a" alt="Step 2"/>
  <br><sub>AI Brain Ready</sub>
</td>
<td align="center">
  <img src="https://img.shields.io/badge/3-Predict-45B7D1?style=for-the-badge&labelColor=1a1a1a" alt="Step 3"/>
  <br><sub>Detect Disease</sub>
</td>
<td align="center">
  <img src="https://img.shields.io/badge/4-Show-96CEB4?style=for-the-badge&labelColor=1a1a1a" alt="Step 4"/>
  <br><sub>View Results</sub>
</td>
</tr>
</table>

</div>

<br>

---

<br>

## 🦠 Supported Plant Diseases (12 Types)

### 🫘 Bean Diseases (2)
- Angular Leaf Spot
- Rust

### 🍓 Strawberry Diseases (7)
- Angular Leaf Spot
- Anthracnose Fruit Rot  
- Blossom Blight
- Gray Mold
- Leaf Spot
- Powdery Mildew (Fruit)
- Powdery Mildew (Leaf)

### 🍅 Tomato Diseases (3)
- Blight
- Leaf Mold  
- Spider Mites

<br>

---

<br>

## 📁 Project Structure

```
Plant-Disease-Detection/
├── main.py                      # Detection script (7 lines)
├── requirements.txt             # Dependencies
├── data.yaml                    # Dataset configuration
├── yolo26n.pt                   # Pre-trained weights
└── runs/detect/train/
    ├── weights/best.pt          # Trained model
    ├── results.png              # Training metrics
    └── confusion_matrix.png     # Performance analysis
```

## ⚙️ Technical Specifications

- **Model**: YOLOv8 Nano (lightweight & fast)
- **Dataset**: 5,493 annotated images
- **Resolution**: 640×640 pixels  
- **Training**: 100 epochs
- **Classes**: 12 disease types

## 🤝 Credits

**Built with:**
- 📊 **Dataset**: [Roboflow Universe](https://universe.roboflow.com/artificial-intelligence-82oex/detecting-diseases/dataset/6) (CC BY 4.0)
- 🧠 **AI Framework**: [Ultralytics YOLOv8](https://github.com/ultralytics/ultralytics)

---

<div align="center">

⭐ **If this helps you, give it a star!**  
*Made with 💚 for smarter agriculture and better crop health*

</div>
