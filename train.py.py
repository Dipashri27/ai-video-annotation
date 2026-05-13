from ultralytics import YOLO

# Load pretrained YOLOv8 model
model = YOLO("yolov8n.pt")

# Train model
model.train(
    data="dataset/data.yaml",
    epochs=50,
    imgsz=640
)