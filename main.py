from ultralytics import YOLO

# model
model = YOLO("yolov8m.pt")

results = model.track(source="https://www.youtube.com/watch?v=2oMXIbOiASI", show=True, tracker="bytetrack.yaml")
