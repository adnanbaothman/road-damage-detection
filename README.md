# Road Damage Detection

AI-based road damage detection using deep learning and the RDD2022 dataset.

## What This Project Does

The project uses a YOLO object-detection model to find four types of road damage:

| Class | Meaning |
| --- | --- |
| D00 | Longitudinal crack |
| D10 | Transverse crack |
| D20 | Alligator crack |
| D40 | Pothole |

The trained model looks at an uploaded road image, predicts damage locations, and draws a box around each prediction.

## Main Folders

- `app/` contains the Streamlit application.
- `reports/baseline/weights/best.pt` is the trained model used by the app.
- `reports/baseline/` contains training results and evaluation images.
- `notebooks/` contains the Colab and Kaggle training notebooks.
- `data/` contains dataset documentation and exploratory analysis files. The full dataset is not stored in this repository because it is large.

## Setup

Create and activate a virtual environment, then install the project dependencies:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

The dependency file contains the libraries used by the application:

- `streamlit` creates the browser-based user interface.
- `ultralytics` loads and runs the YOLO model.
- `Pillow` reads uploaded image files.
- `numpy` converts images into arrays that the model can process.

## Run the Application

Run this command from the repository root:

```powershell
streamlit run app/app.py
```

Then open the local URL shown in the terminal, upload a JPG, JPEG, or PNG road image, and review the predicted damage boxes and confidence scores.

## Model Results

The baseline model achieved approximately 0.603 mAP@0.5 on the validation set. Performance is not identical across classes: D20 performs best, while D40 has lower recall and may miss potholes.

## Saudi External-Domain Evaluation

The final RoadGuard model was also tested on unseen Saudi road imagery as an external-domain evaluation.

- Saudi pothole-positive images evaluated: 4,923
- Images with at least one RoadGuard prediction: 894
- Prediction presence rate at confidence 0.26: 18.16%
- The Saudi dataset was not used for model training.
- Because its annotation scheme differs from RDD2022, this result is reported as prediction presence rather than directly comparable mAP or accuracy.

Full Saudi evaluation files:
reports/saudi_evaluation/
