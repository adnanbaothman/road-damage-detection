from ultralytics import YOLO

DATA_YAML = "/content/rdd2022_yolo/data_d40_2x.yaml"

model = YOLO("yolo11s.pt")

results = model.train(
    data=DATA_YAML,
    epochs=50,
    imgsz=640,
    batch=32,
    device=0,
    patience=10,
    optimizer="auto",
    seed=0,
    translate=0.1,
    scale=0.5,
    fliplr=0.5,
    mosaic=1.0,
    mixup=0.0,
    project="/content/drive/MyDrive/NEXORA/RoadDamageProject/experiments",
    name="experiment_01_d40_2x",
    save=True,
)