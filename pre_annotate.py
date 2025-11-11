import os
import json
import cv2
from ultralytics import YOLO

# ---------------------------------------------------
# STEP 1: Define paths
# ---------------------------------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # the folder this script lives in

model_path = os.path.join(BASE_DIR, "yolov11n_best.pt")
frames_dir = os.path.join(BASE_DIR, "frames")
output_json = os.path.join(BASE_DIR, "pre_annotations.json")

# Load YOLO model
model = YOLO(model_path)
all_predictions = []

# ---------------------------------------------------
# STEP 2: Process each frame
# ---------------------------------------------------
for img_name in sorted(os.listdir(frames_dir)):
    if not img_name.lower().endswith(".jpg"):
        continue

    img_path = os.path.join(frames_dir, img_name)
    img = cv2.imread(img_path)
    if img is None:
        print(f"⚠️ Skipping unreadable image: {img_name}")
        continue

    height, width = img.shape[:2]
    results = model(img_path)[0]

    # Build Label Studio JSON structure
    prediction = {
        "data": {
            "image": f"/data/local-files/?d={img_path}"  # ✅ absolute path
        },
        "predictions": [
            {
                "model_version": "yolov11-prelabel",
                "result": []
            }
        ]
    }

    # Add all detection boxes
    for box in results.boxes:
        x1, y1, x2, y2 = box.xyxy[0]
        cls = int(box.cls[0])
        label = model.names[cls]
        conf = float(box.conf[0])

        # Convert coords to percentages
        x = float(x1 / width * 100)
        y = float(y1 / height * 100)
        w = float((x2 - x1) / width * 100)
        h = float((y2 - y1) / height * 100)

        prediction["predictions"][0]["result"].append({
            "type": "rectanglelabels",
            "from_name": "label",
            "to_name": "image",
            "value": {
                "x": x,
                "y": y,
                "width": w,
                "height": h,
                "rectanglelabels": [label]
            },
            "score": conf
        })

    all_predictions.append(prediction)
    print(f"✅ Processed {img_name}")

# ---------------------------------------------------
# STEP 3: Save JSON file
# ---------------------------------------------------
with open(output_json, "w") as f:
    json.dump(all_predictions, f, indent=2)

print(f"🎉 Pre-annotations saved to: {output_json}")
