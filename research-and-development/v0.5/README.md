# RoadGuard AI R&D v0.5
## D40-Focused Improvement Experiment

### Problem

Baseline evaluation identified D40 (Pothole) as the weakest class.

Baseline D40 metrics:

- Recall: 0.439
- mAP@0.5: 0.520
- mAP@0.5:0.95: 0.240
- True Positives: 261
- False Negatives: 375
- Misclassifications: 6

### Training Dataset Analysis

Training instances:

- D00: 20,800
- D10: 9,504
- D20: 8,464
- D40: 5,243

Total training images: 30,707

Images containing D40: 2,938

Only 9.57% of training images contain at least one D40 instance.

### Hypothesis

Increasing exposure to D40-containing training images may improve
D40 recall and reduce false negatives.

### Experiment 1

D40-containing images are oversampled 2x.

Original training images:
30,707

D40-containing images:
2,938

Experiment training entries:
33,645

Validation and test datasets remain unchanged.

### Primary Targets

Baseline:

D40 Recall = 0.439
D40 mAP50 = 0.520
D40 mAP50-95 = 0.240
Overall mAP50 = 0.601

Experiment 1 will be considered useful if D40 recall and mAP improve
without causing a significant decrease in overall model performance.

### Status

Dataset preparation: In progress
Training: Not started
Evaluation: Not started