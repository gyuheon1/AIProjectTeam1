from ultralytics import YOLO
URL=f"./AIProjetTeam1-15/data.yaml"
model = YOLO(task="detect", model="yolov8n.pt")

model.train(data=URL, epochs=100, imgsz=640)