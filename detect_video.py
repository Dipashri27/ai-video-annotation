import cv2
from ultralytics import YOLO
import os

# Load Custom Trained Model
model = YOLO("runs/detect/train-2/weights/best.pt")

# Input Video
video_path = "input.mp4"

if not os.path.exists(video_path):
    print("Error: input.mp4 not found")
    exit()

cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("Error: Could not open video")
    exit()

# Video Properties
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)

# Create Output Folder
os.makedirs("outputs", exist_ok=True)

output_path = "outputs/output.avi"

fourcc = cv2.VideoWriter_fourcc(*'XVID')

out = cv2.VideoWriter(
    output_path,
    fourcc,
    fps,
    (frame_width, frame_height)
)

print("Processing Video...")

while True:

    ret, frame = cap.read()

    if not ret:
        break

    # Run Detection
    results = model(frame)

    # Draw Results
    annotated_frame = results[0].plot()

    # Save Frame
    out.write(annotated_frame)

    # Show Frame
    cv2.imshow("Helmet Detection", annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()

print(f"Output saved at: {output_path}")