import cv2
from ultralytics import YOLO

# Load Custom Trained Model
model = YOLO("runs/detect/train-2/weights/best.pt")

# Open Webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Cannot access webcam")
    exit()

print("Press 'q' to quit")

while True:
    ret, frame = cap.read()

    if not ret:
        break

    # Run Detection
    results = model(frame)

    # Draw Bounding Boxes
    annotated_frame = results[0].plot()

    # Display Output
    cv2.imshow("Helmet Detection", annotated_frame)

    # Quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()