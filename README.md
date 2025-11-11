# 🎥 VideoToDataset Pipeline

A reusable Python pipeline for converting grocery-store videos into labeled datasets for computer vision training.  
This project supports both **manual annotation** and **semi-automated pre-labeling using YOLOv11** with Label Studio.

---

## 🧠 Features

- Extracts frames from a video (`.MOV` or `.MP4`) at a configurable interval  
- Runs object detection using a pre-trained YOLOv11 model (`yolov11n_best.pt`)  
- Generates a `pre_annotations.json` file compatible with Label Studio  
- Allows fast dataset creation and model improvement workflows  
- Exportable to COCO format for training on future models  

---

## 🚀 How to Use

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/RahulBassi/VideoToDataset.git
cd VideoToDataset
