# 🎥 AI Video Annotation & Helmet Detection System

An AI-powered Computer Vision project using YOLOv8 and OpenCV for real-time object detection, video annotation, and helmet detection.

This system detects:
- 👤 Person
- 🚗 Car
- 🏍 Bike
- 🚛 Truck
- 🚌 Bus
- 🪖 Helmet
- ❌ No Helmet

The project supports:
- Real-time webcam detection
- Video annotation
- Custom model training
- Bounding box visualization
- Deep learning-based object detection

---

# 🚀 Features

✅ Real-time object detection  
✅ Helmet and No-Helmet detection  
✅ Video annotation with bounding boxes  
✅ Webcam live detection  
✅ Custom YOLOv8 model training  
✅ Output video saving  
✅ Deep learning-based detection  
✅ Transfer learning using pretrained YOLOv8  

---

# 🛠 Technologies Used

- Python
- OpenCV
- YOLOv8
- Ultralytics
- NumPy

---

# 📂 Project Structure

```bash
AI-VIDEO-ANNOTATION-TOOL/
│
├── dataset/
│   ├── train/
│   ├── valid/
│   ├── test/
│   └── data.yaml
│
├── runs/
│
├── screenshots/
│
├── detect_video.py
├── detect_webcam.py
├── train.py
├── requirements.txt
├── README.md
├── input.mp4
├── output.avi
└── yolov8n.pt
```

---

# 📦 Installation

## 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/AI-VIDEO-ANNOTATION-TOOL.git
```

---

## 2️⃣ Open Project Folder

```bash
cd AI-VIDEO-ANNOTATION-TOOL
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Run Object Detection

## 🎥 Video Detection

```bash
python detect_video.py
```

---

## 📷 Webcam Detection

```bash
python detect_webcam.py
```

---

# 🧠 Train Custom Model

## Run Training

```bash
python train.py
```

---

# 📁 Dataset Format

```bash
dataset/
│
├── train/
│   ├── images/
│   └── labels/
│
├── valid/
│   ├── images/
│   └── labels/
│
├── test/
│   ├── images/
│   └── labels/
│
└── data.yaml
```

---

# 📝 Example data.yaml

```yaml
path: dataset

train: train/images
val: valid/images
test: test/images

names:
  0: helmet
  1: no_helmet
```

---

# 🎯 Model Training

This project uses:
- Transfer Learning
- YOLOv8 pretrained weights
- Custom helmet detection dataset

Training improves:
- Helmet accuracy
- Object recognition
- Real-world detection performance

---

# 📸 Output Example

The system detects and annotates:
- Persons
- Vehicles
- Helmets
- Traffic objects

with bounding boxes in real-time.

---

# 🚀 Future Improvements

- Object Tracking
- Vehicle Counting
- Accident Detection
- Traffic Monitoring
- Flask Web Application
- AI Surveillance System

---

# 📊 Applications

- Smart Traffic Monitoring
- Helmet Safety Detection
- CCTV Surveillance
- Road Safety Systems
- AI Video Analytics

---

# 👩‍💻 Author

Dipashri Solanker

---

# ⭐ GitHub Topics

```txt
artificial-intelligence
computer-vision
deep-learning
yolov8
opencv
helmet-detection
object-detection
python
video-annotation
machine-learning
```

---

