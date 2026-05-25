from ultralytics import YOLO

model = YOLO("runs/detect/train-2/weights/best.pt")

print("Model Classes:")
print(model.names)