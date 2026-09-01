# YOLO11s Baseline — RDD2022 Road Damage Detection

This folder contains the outputs of the **YOLO11s baseline training run** for the RDD2022 road damage detection project.

## 1. Baseline Model

- **Model:** YOLO11s
- **Initialization:** COCO-pretrained weights
- **Task:** Object Detection
- **Input image size:** 640
- **Batch size:** 32
- **Epochs:** 50
- **Validation split:** `val`
- **Target classes:** D00, D10, D20, D40

### Class Definitions

| Class | Damage Type |
|---|---|
| D00 | Longitudinal Crack |
| D10 | Transverse Crack |
| D20 | Alligator Crack |
| D40 | Pothole |

The full training configuration is available in `args.yaml`.

---

## 2. Validation Results

The following results were obtained using the baseline model on the validation set.

| Class | Precision | Recall | mAP@0.5 | mAP@0.5:0.95 |
|---|---:|---:|---:|---:|
| **All** | **0.668** | **0.548** | **0.603** | **0.317** |
| D00 | 0.643 | 0.546 | 0.586 | 0.339 |
| D10 | 0.636 | 0.563 | 0.597 | 0.302 |
| D20 | 0.705 | 0.643 | 0.703 | 0.388 |
| D40 | 0.687 | 0.439 | 0.525 | 0.240 |

- **Best-performing class:** D20
- **Weakest class:** D40
- **Inference time:** approximately 5.3 ms/image

The F1-Confidence curve shows an overall best F1 of approximately **0.60** at a confidence threshold of approximately **0.26**.

---

## 3. Included Files

### Model Weights

- `best.pt` — best checkpoint from the baseline training run; use this file for evaluation and further experiments.
- `last.pt` — final checkpoint at the end of training; retained for reproducibility and possible resume use.

### Training Configuration and Metrics

- `args.yaml` — full Ultralytics training configuration.
- `results.csv` — epoch-by-epoch training and validation metrics.
- `results.png` — training/validation losses and metric curves.

### Evaluation Plots

- `BoxF1_curve.png` — F1 score versus confidence threshold.
- `BoxP_curve.png` — precision versus confidence threshold.
- `BoxR_curve.png` — recall versus confidence threshold.
- `BoxPR_curve.png` — precision-recall curve.
- `confusion_matrix.png` — raw confusion matrix.
- `confusion_matrix_normalized.png` — normalized confusion matrix.

### Dataset / Batch Visualizations

- `labels.jpg` — class and bounding-box distribution visualization.
- `train_batch38400.jpg`
- `train_batch38401.jpg`
- `train_batch38402.jpg`

These training-batch images provide examples of the training data and labels used during training.

### Validation Examples

- `val_batch0_labels.jpg`
- `val_batch0_pred.jpg`
- `val_batch1_labels.jpg`
- `val_batch1_pred.jpg`
- `val_batch2_labels.jpg`
- `val_batch2_pred.jpg`

The `*_labels.jpg` files show the ground-truth annotations, while the corresponding `*_pred.jpg` files show the baseline model predictions.

---

## 4. Purpose of This Baseline

This baseline is the reference point for all later model-improvement experiments.

Any future experiment should be compared against this baseline using the same validation split and the same evaluation metrics.

Example experiment naming:

- `BASE-01` — current YOLO11s baseline
- `AUG-01` — augmentation experiment
- `IMB-01` — class-imbalance treatment experiment
- `TUNE-01` — hyperparameter / confidence tuning experiment
- `FINAL-01` — final selected model

These names are only used to organize experiments; they do not indicate that these experiments have already been completed.

---

## 5. Next Step — Evaluation & Error Analysis

The next stage should use `best.pt` and the existing validation results to perform a deeper evaluation of the baseline.

The evaluation should focus on:

- Per-class Precision, Recall, mAP@0.5, and mAP@0.5:0.95.
- Confusion matrix interpretation.
- False positives and false negatives.
- Misclassification patterns.
- Weak-class analysis, especially D40.
- Confidence-threshold analysis.
- Potential effects of class imbalance.
- Evidence-based recommendations for augmentation, imbalance treatment, or tuning.

The existing plots and validation prediction images in this folder should be used as the starting point rather than repeating the baseline training.

> **Important:** Use the validation set for analysis, tuning, and experiment selection. Keep the held-out test set for the final evaluation after the final model configuration has been selected.

---

## 6. Reproducibility Notes

The baseline was trained with Ultralytics YOLO using the configuration saved in `args.yaml`.

For reproducibility, future experiments should clearly record:

- model/checkpoint used,
- dataset split,
- training parameters,
- augmentation settings,
- confidence threshold,
- validation metrics,
- and the exact change made relative to `BASE-01`.

This ensures that every improvement can be compared fairly against the original baseline.
