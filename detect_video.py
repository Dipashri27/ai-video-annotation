import cv2
from ultralytics import YOLO
import os

# Load YOLO model
model = YOLO("yolov8n.pt")

# Input video path
video_path = "input.mp4"

# Check if input video exists
if not os.path.exists(video_path):
    print("Error: Input video file not found")
    exit()

# Open input video
cap = cv2.VideoCapture(video_path)

# Check if video opened successfully
if not cap.isOpened():
    print("Error: Could not open video")
    exit()

# Get video properties
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)

# Debug information
print("Width:", frame_width)
print("Height:", frame_height)
print("FPS:", fps)

# Validate dimensions
if frame_width == 0 or frame_height == 0:
    print("Error: Invalid video dimensions")
    exit()

# Create output folder
os.makedirs("outputs", exist_ok=True)

# Output video path
output_path = "outputs/output.avi"

# Define codec
fourcc = cv2.VideoWriter_fourcc(*'XVID')

# Create VideoWriter object
out = cv2.VideoWriter(
    output_path,
    fourcc,
    fps,
    (frame_width, frame_height)
)

# Check if VideoWriter initialized
if not out.isOpened():
    print("Error: VideoWriter failed to initialize")
    exit()

print("Processing video...")

while cap.isOpened():

    ret, frame = cap.read()

    if not ret:
        print("Video processing completed")
        break

    # Run YOLO detection
    results = model(frame)

    # Draw bounding boxes
    annotated_frame = results[0].plot()

    # Write frame to output video
    out.write(annotated_frame)

    # Display frame
    cv2.imshow("AI Video Annotation", annotated_frame)

    # Press q to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
out.release()
cv2.destroyAllWindows()

print("Output video saved at:", output_path)