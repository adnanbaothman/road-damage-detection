# `app.py` Guide

This folder contains the Streamlit application in [`app.py`](app.py). The file is the user interface and inference entry point for the road damage detection prototype.

## Purpose of `app.py`

The script lets a user upload a road image and uses the trained YOLO model to:

1. Read the uploaded image.
2. Detect road damage in the image.
3. Draw prediction boxes on the image.
4. Display each detected class and its confidence score.

The supported model classes are D00, D10, D20, and D40.

## Imports

```python
import streamlit as st
from ultralytics import YOLO
from PIL import Image
import numpy as np
from pathlib import Path
```

- `streamlit` builds the web page and handles uploads, messages, buttons, and reruns.
- `YOLO` loads the trained Ultralytics model and performs object detection.
- `Image` opens the uploaded image file.
- `numpy` converts the PIL image into an array that YOLO can process.
- `Path` builds the model path reliably on different operating systems and launch folders.

## Model Loading and Caching

```python
@st.cache_resource
def load_model(model_path):
	return YOLO(model_path)
```

Streamlit reruns the script whenever the user uploads an image or clicks a button. `st.cache_resource` keeps the loaded model in memory so the application does not load the model again on every rerun.

The model is located relative to this file:

```python
Path(__file__).resolve().parent.parent / "reports" / "baseline" / "weights" / "best.pt"
```

This means the app expects `best.pt` at `reports/baseline/weights/best.pt` in the repository. The app does not depend on the folder from which Streamlit was started.

## Page and Styling

`st.set_page_config` sets the browser title, icon, and centered layout. The CSS passed to `st.markdown` defines the visual appearance of the title, subtitle, result headings, prediction cards, and footer.

The HTML is rendered with `unsafe_allow_html=True` because the app uses custom CSS classes and HTML elements. Only fixed application text and model class names are inserted into these blocks.

## Upload Handling

The uploader accepts only `.jpg`, `.jpeg`, and `.png` files. Streamlit stores the uploaded file in `uploaded_file`.

The `uploader_key` value in `st.session_state` is used to reset the uploader after the user clicks **Delete Image**. Increasing the key creates a fresh uploader after `st.rerun()`.

## Detection Flow

When `uploaded_file` is not `None`:

1. `Image.open` reads the uploaded file.
2. `np.array(image)` converts it to a NumPy array.
3. `load_model(model_path)` returns the cached YOLO model.
4. `model(image_array)` runs inference using the model's default image size and settings.
5. `results[0].plot()` creates an annotated image with the predicted boxes and labels.

The first result is used because one image is submitted at a time.

## Displaying Predictions

`results[0].boxes` contains the detected objects. For each box, the app reads:

- `box.cls[0]`: the numeric class ID,
- `box.conf[0]`: the confidence score, and
- `model.names[class_id]`: the human-readable class name.

The confidence value is multiplied by 100 and displayed as a percentage. If there are no boxes, the app displays `No objects detected.`

## Run the App

Run this command from the repository root:

```powershell
streamlit run app/app.py
```

Then open the local URL shown by Streamlit, normally `http://localhost:8501`.

## Maintenance Notes

- Edit [`app.py`](app.py), not generated files such as `__pycache__/app.cpython-*.pyc`.
- Keep `reports/baseline/weights/best.pt` available when running the app.
- The model runs on whatever device Ultralytics selects in the current environment. CPU machines will generally be slower than GPU machines.
- If the model location changes, update the `model_path` expression in `app.py` and this guide together.
