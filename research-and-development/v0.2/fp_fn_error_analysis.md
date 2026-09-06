# RoadGuard AI R&D v0.2 - FP/FN Error Analysis

## Objective

Move from general model metrics to instance-level diagnosis by comparing baseline predictions against the validation ground truth.

## Evaluation basis

- Validation images: 3,833
- Model: `reports/baseline/weights/best.pt`
- Confidence threshold: 0.26
- Matching rule: IoU >= 0.50
- Classes: D00, D10, D20, D40

## Error definitions

- True Positive (TP): a prediction overlaps a ground-truth box by at least the IoU threshold and has the correct class.
- False Negative (FN): a ground-truth damage instance has no matching prediction.
- False Positive (FP): a prediction has no matching ground-truth instance.
- Misclassification: location matches a ground-truth instance but the predicted class is different.

## Results

| Class | TP | FP | FN | Misclassification |
|---|---:|---:|---:|---:|
| D00 | 1,299 | 682 | 1,235 | 26 |
| D10 | 621 | 315 | 546 | 15 |
| D20 | 660 | 226 | 380 | 21 |
| D40 | 261 | 98 | 375 | 6 |

## Main finding

D40 shows the most severe missed-detection problem. Using the diagnostic matching rule, 375 D40 instances were false negatives compared with 261 true positives. Misclassification is relatively small, so the main problem is not class confusion; it is failure to detect the object at all.

The D40 miss proportion in this diagnostic count is approximately 58.4% when calculated as FN / (TP + FN + Misclassification).

## Improvement direction

The first controlled model-improvement experiment should focus on D40 representation and difficult examples, while keeping validation and test splits unchanged. Candidate interventions include:

- D40-focused sampling or moderate oversampling
- realistic brightness/contrast augmentation
- small scaling and translation
- mild blur where representative of field conditions
- review of D40 label quality

Do not change many variables at once. The primary comparison targets are D40 Recall > 0.439 and D40 mAP50 > 0.520 without a major precision drop.
