<div align="center">

# � Plant Disease Detection AI

<p align="center">
  <img src="https://img.shields.io/badge/YOLOv26-Ready_to_Deploy-00D2FF?style=for-the-badge&labelColor=1a1a1a" alt="Status"/>
  <img src="https://img.shields.io/badge/Accuracy-91.67%25-4CAF50?style=for-the-badge&labelColor=1a1a1a" alt="Accuracy"/>
  <img src="https://img.shields.io/badge/Diseases-12_Types-FF6B6B?style=for-the-badge&labelColor=1a1a1a" alt="Disease Types"/>
</p>

### 🚀 **AI-Powered Plant Disease Detection in 7 Lines of Code**

**ตรวจจับโรคพืช 12 ชนิด จากภาพถ่าย ด้วย YOLOv26 ที่เทรนจาก 5,500+ ภาพ**

<br>

<p align="center">
  <img src="https://img.shields.io/badge/🫘_Bean-2_Diseases-8BC34A?style=flat-square" alt="Bean"/>
  <img src="https://img.shields.io/badge/🍓_Strawberry-7_Diseases-E91E63?style=flat-square" alt="Strawberry"/>
  <img src="https://img.shields.io/badge/🍅_Tomato-3_Diseases-FF5722?style=flat-square" alt="Tomato"/>
</p>

---

## ⚡ **Quick Start - 3 Steps**

```bash
# 1️⃣ Clone & Install
git clone https://github.com/0x90Vold/Plant-Disease-Detection.git
cd Plant-Disease-Detection
pip install ultralytics

# 2️⃣ Replace "leaf_photo.jpg" with your image
# 3️⃣ Run Detection
python main.py
```

**That's it! 🎉 The AI will detect diseases and show results**

</div>

<br>

---

<br>

## 🎯 **Performance Metrics**

<div align="center">

<table>
<tr>
<td align="center">
  <img src="https://img.shields.io/badge/mAP50-91.67%25-4CAF50?style=for-the-badge&labelColor=1a1a1a" alt="mAP50"/>
  <br><sub>Primary Accuracy</sub>
</td>
<td align="center">
  <img src="https://img.shields.io/badge/Precision-91.85%25-2196F3?style=for-the-badge&labelColor=1a1a1a" alt="Precision"/>
  <br><sub>True Positive Rate</sub>
</td>
<td align="center">
  <img src="https://img.shields.io/badge/Recall-86.78%25-FF9800?style=for-the-badge&labelColor=1a1a1a" alt="Recall"/>
  <br><sub>Disease Detection Rate</sub>
</td>
<td align="center">
  <img src="https://img.shields.io/badge/mAP50--95-77.15%25-9C27B0?style=for-the-badge&labelColor=1a1a1a" alt="mAP50-95"/>
  <br><sub>Overall Accuracy</sub>
</td>
</tr>
</table>

<br>

**🏆 Trained on 5,493 images • 100 epochs • YOLOv26 Nano**

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

## 🦠 **Supported Plant Diseases**

<div align="center">

### **12 Disease Types Across 3 Crops**

<br>

<table>
<tr>
<td align="center" width="33%">

<img src="https://img.shields.io/badge/🫘_BEAN_DISEASES-2_Types-8BC34A?style=for-the-badge&labelColor=1a1a1a" alt="Bean Diseases"/>

<br><br>

• **Angular Leaf Spot**  
• **Rust**

</td>
<td align="center" width="33%">

<img src="https://img.shields.io/badge/🍓_STRAWBERRY_DISEASES-7_Types-E91E63?style=for-the-badge&labelColor=1a1a1a" alt="Strawberry Diseases"/>

<br><br>

• **Angular Leaf Spot**  
• **Anthracnose Fruit Rot**  
• **Blossom Blight**  
• **Gray Mold**  
• **Leaf Spot**  
• **Powdery Mildew (Fruit)**  
• **Powdery Mildew (Leaf)**

</td>
<td align="center" width="33%">

<img src="https://img.shields.io/badge/🍅_TOMATO_DISEASES-3_Types-FF5722?style=for-the-badge&labelColor=1a1a1a" alt="Tomato Diseases"/>

<br><br>

• **Blight**  
• **Leaf Mold**  
• **Spider Mites**

</td>
</tr>
</table>

</div>

<br>

---

<br>

## � **Project Structure**

```bash
� Plant-Disease-Detection/
│
├── � main.py                    # 7-line detection script
├── ⚙️ requirements.txt           # Dependencies  
├── � data.yaml                  # Dataset config
├── 🧠 yolo26n.pt                 # Pre-trained weights
│
├── 📁 runs/detect/train/         # Training results
│   ├── 🎯 weights/best.pt        # Trained model (ready to use!)
│   ├── 📈 results.png            # Training graphs
│   ├── 🔍 confusion_matrix.png   # Performance analysis  
│   └── 📊 validation_results/    # Prediction examples
│
└── 📁 train/valid/test/          # Dataset (5,493 images)
```

---

## ⚡ **Technical Specifications**

<div align="center">

<table>
<tr>
<td align="center">
  <img src="https://img.shields.io/badge/Model-YOLOv26_Nano-00D2FF?style=for-the-badge&labelColor=1a1a1a" alt="Model"/>
  <br><sub>Lightweight & Fast</sub>
</td>
<td align="center">
  <img src="https://img.shields.io/badge/Dataset-5,493_Images-4CAF50?style=for-the-badge&labelColor=1a1a1a" alt="Dataset"/>
  <br><sub>High Quality Data</sub>
</td>
<td align="center">
  <img src="https://img.shields.io/badge/Resolution-640×640-FF9800?style=for-the-badge&labelColor=1a1a1a" alt="Resolution"/>
  <br><sub>Optimal Balance</sub>
</td>
<td align="center">
  <img src="https://img.shields.io/badge/Training-100_Epochs-9C27B0?style=for-the-badge&labelColor=1a1a1a" alt="Training"/>
  <br><sub>Fully Converged</sub>
</td>
</tr>
</table>

</div>

---

## 🤝 **Credits & Acknowledgments**

<div align="center">

<br>

**Built with powerful open-source tools**

<br>

<table>
<tr>
<td align="center" width="50%">
  <img src="https://img.shields.io/badge/Dataset_by-Roboflow-6706CE?style=for-the-badge&logo=roboflow&logoColor=white&labelColor=1a1a1a" alt="Roboflow"/>
  <br><br>
  <sub>High-quality annotated dataset from <a href="https://universe.roboflow.com/artificial-intelligence-82oex/detecting-diseases/dataset/6">Roboflow Universe</a></sub>
</td>
<td align="center" width="50%">
  <img src="https://img.shields.io/badge/AI_Framework-Ultralytics-00D2FF?style=for-the-badge&logo=yolo&logoColor=white&labelColor=1a1a1a" alt="Ultralytics"/>
  <br><br>
  <sub>YOLOv26 model powered by <a href="https://github.com/ultralytics/ultralytics">Ultralytics</a></sub>
</td>
</tr>
</table>

<br><br>

---

<br>

<img src="https://img.shields.io/badge/⭐_If_this_helps_you-Give_it_a_Star!-FFD700?style=for-the-badge&labelColor=1a1a1a" alt="Star"/>

<br>

<sub>**Made with 💚 for smarter agriculture and better crop health**</sub>

<br><br>

</div>
