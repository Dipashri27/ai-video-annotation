import cv2
from ultralytics import YOLO

# Load YOLO model
model = YOLO("yolov8n.pt")

# Open input video
cap = cv2.VideoCapture("input.mp4")

# Get video properties
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
fps = int(cap.get(cv2.CAP_PROP_FPS))

# Save output video
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, fps, (frame_width, frame_height))

while cap.isOpened():
    ret, frame = cap.read()

    if not ret:
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

cap.release()
out.release()
cv2.destroyAllWindows()