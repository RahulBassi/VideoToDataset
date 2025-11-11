import cv2
import os

# Path to your video
video_path = "/Users/rahulbassi/Desktop/VideoToDataset/video/IMG_9104.MOV"

# Folder to save extracted frames
output_folder = "/Users/rahulbassi/Desktop/VideoToDataset/frames"
os.makedirs(output_folder, exist_ok=True)

# Open the video
capture = cv2.VideoCapture(video_path)

# Frame counter
f = 0

# Loop through video frames
while capture.isOpened():
    ret, frame = capture.read()
    if not ret:
        break

    # Save every 30th frame
    if f % 30 == 0:
        filename = os.path.join(output_folder, f"frame_{f:04d}.jpg")
        cv2.imwrite(filename, frame)
        print(f"Saved {filename}")

    f += 1

capture.release()
print("✅ Done! Frames saved to", output_folder)
