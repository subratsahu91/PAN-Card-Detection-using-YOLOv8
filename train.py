from ultralytics import YOLO

def main():
    # Load YOLO pretrained model
    model = YOLO("yolov8n.pt")

    # Train the model
    model.train(
    data="data.yaml",
    epochs=10,
    imgsz=416,
    batch=8
)

if __name__ == "__main__":
    main()