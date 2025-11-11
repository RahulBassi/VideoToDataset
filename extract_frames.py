import cv2
import os

# ---------------------------------------------------
# STEP 1: Define paths (relative paths for portability)
# ---------------------------------------------------

# Base directory where this script lives
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Path to your video (inside the 'video' folder)
video_path = os.path.join(BASE_DIR, "video", "IMG_9104.MOV")

# Folder to save extracted frames
output_folder = os.path.join(BASE_DIR, "frames")
os.makedirs(output_folder, exist_ok=True)

# ---------------------------------------------------
# STEP 2: Open the video
# ---------------------------------------------------

capture = cv2.VideoCapture(video_path)
if not capture.isOpened():
    raise IOError(f"❌ Could not open video file: {video_path}")

# Frame counter
f = 0

# ---------------------------------------------------
# STEP 3: Extract and save frames
# ---------------------------------------------------

while capture.isOpened():
    ret, frame = capture.read()
    if not ret:
        break

    # Save every 30th frame (you can adjust the interval)
    if f % 30 == 0:
        filename = os.path.join(output_folder, f"frame_{f:04d}.jpg")
        cv2.imwrite(filename, frame)
        print(f"✅ Saved {filename}")

    f += 1

# ---------------------------------------------------
# STEP 4: Clean up
# ---------------------------------------------------

capture.release()
print(f"🎉 Done! Extracted frames saved in: {output_folder}")
