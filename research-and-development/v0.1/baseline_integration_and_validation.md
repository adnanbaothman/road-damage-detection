# RoadGuard AI R&D v0.1 - Baseline Integration and Validation

## Objective

Connect the Streamlit prototype to the actual road-damage model and establish the first reproducible baseline.

## Prototype issue discovered

The first version of `app/app.py` loaded the generic pretrained model:

```python
model = YOLO("yolov8n.pt")
```

That model is designed for general object classes such as people and vehicles, not the RoadGuard damage classes.

## Integration change

The application was changed to load the project-trained weights:

```python
BASE_DIR = Path(__file__).resolve().parents[1]
MODEL_PATH = BASE_DIR / "reports" / "baseline" / "weights" / "best.pt"
model = YOLO(str(MODEL_PATH))
```

Input handling was also made explicit:

```python
image = Image.open(uploaded_file).convert("RGB")
image_array = np.array(image)
results = model(image_array, conf=0.26)
```

## Supported classes

- D00 - Longitudinal Crack
- D10 - Transverse Crack
- D20 - Alligator Crack
- D40 - Pothole

## Baseline validation

The full validation split contains 3,833 images and 5,445 labeled damage instances.

| Class | Precision | Recall | mAP50 | mAP50-95 | Instances |
|---|---:|---:|---:|---:|---:|
| All | 0.669 | 0.547 | 0.601 | 0.318 | 5,445 |
| D00 | 0.644 | 0.545 | 0.586 | 0.339 | 2,560 |
| D10 | 0.635 | 0.562 | 0.596 | 0.302 | 1,182 |
| D20 | 0.706 | 0.643 | 0.703 | 0.389 | 1,061 |
| D40 | 0.691 | 0.439 | 0.520 | 0.240 | 642 |

## Initial finding

D20 is the strongest class. D40 is the weakest class, especially in recall. This suggested that missed potholes should be investigated before retraining.
