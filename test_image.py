from ultralytics import YOLO

model = YOLO("runs/detect/train-2/weights/best.pt")

results = model.predict(
    source="dataset/train/images",
    save=True,
    conf=0.05
)

print("Prediction Complete")