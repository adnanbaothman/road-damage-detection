
# RoadGuard AI — Final Evaluation Package

## Final Model

YOLO11s pretrained on COCO and trained on RDD2022.

The selected final model uses D40-focused oversampling.

Training images before oversampling: 30,707

Training images containing D40: 2,938

Effective training entries after repeating D40-containing images:
33,645

Validation and test sets were unchanged.

---

## Validation

Baseline:

Precision: 0.668

Recall: 0.548

mAP@50: 0.603

mAP@50:95: 0.317

Improved:

Precision: 0.664

Recall: 0.552

mAP@50: 0.608

mAP@50:95: 0.322

The improvement was modest overall.

The main targeted improvement was D40 recall:

Baseline D40 Recall: 0.439

Improved D40 Recall: 0.491

This improvement was accompanied by a precision trade-off.

---

## D40 Error Analysis

Operational confidence threshold: 0.26

Matching IoU threshold: 0.50

Baseline:
TP 261
FP 98
FN 375

Improved:
TP 309
FP 184
FN 327

The improved model detected 48 additional true D40 instances
and reduced D40 false negatives by 48, while increasing false positives.

---

## Final Held-Out Test

Images: 3,845

Instances: 5,550

Precision: 0.648

Recall: 0.542

mAP@50: 0.593

mAP@50:95: 0.305

D20 was the strongest test class.

D40 remained the most challenging test class.

---

## Efficiency

Model size: 18.29 MB

Parameters: 9,429,340

GFLOPs: 21.4

Ultralytics test inference time: 9.5 ms/image

Independent end-to-end mean latency: 12.71 ms/image

Approximate throughput: 78.7 images/second

Device: Tesla T4

Image size: 640


## Saudi External-Domain Check

Saudi pothole-road images evaluated: 4923

Images with at least one RoadGuard prediction:
894

Images with no RoadGuard prediction:
4029

Prediction presence rate:
18.16%

Confidence threshold: 0.26

This Saudi experiment is treated as an external-domain prediction
check rather than a four-class mAP evaluation because the Saudi
dataset and RDD2022 use different class definitions and annotation
schemes.

The purpose of this check is to determine whether the RDD2022-trained
RoadGuard model can produce road-damage detections on unseen Saudi
road imagery.


---

## Important Evaluation Note

The RDD2022 held-out test set was used only after model selection
based on validation results.

The Saudi dataset was not used for training.

The Saudi experiment is therefore an external-domain check.

