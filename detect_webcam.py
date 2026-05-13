import cv2
from ultralytics import YOLO

# Load YOLO model
model = YOLO("yolov8n.pt")

# Open webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    if not ret:
        break

    # Object detection
    results = model(frame)

    # Draw annotations
    annotated_frame = results[0].plot()

    cv2.imshow("Live Object Detection", annotated_frame)

    # Exit using q
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

