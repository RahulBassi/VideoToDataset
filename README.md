# 🎥 Video-to-Dataset Converter

This repository converts a video into a set of image frames and uses a YOLOv11 model to automatically generate pre-annotations for Label Studio.

---

## 🧠 Features
- Extracts frames from a `.MOV` video file at a configurable interval  
- Runs object detection using a YOLOv11 model (`yolov11n_best.pt`)  
- Exports detections into a `pre_annotations.json` file compatible with Label Studio  
- Enables quick dataset generation for labeling or model fine-tuning

---

## 🚀 How to Use

### 1️⃣ Setup
Clone the repo:
```bash
git clone https://github.com/Perceive-AI/Video-to-Dataset.git
cd Video-to-Dataset
