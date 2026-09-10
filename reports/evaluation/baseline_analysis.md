# Baseline Evaluation – Initial Analysis

## Current Baseline

The YOLO11s baseline training has been completed and the existing
validation results were reviewed.

### Overall Performance

The Precision–Recall curve reports an overall:

- mAP@0.5: 0.603

Per-class AP@0.5:

| Class | Damage Type | AP@0.5 |
|------|-------------|-------|
| D00 | Longitudinal Crack | 0.586 |
| D10 | Transverse Crack | 0.597 |
| D20 | Alligator Crack | 0.703 |
| D40 | Pothole | 0.525 |

D20 currently has the strongest baseline performance, while D40
has the weakest performance.

## Confusion Matrix Analysis

The normalized confusion matrix indicates that most errors are
missed detections rather than confusion between damage classes.

Approximate correct detection rates from the diagonal are:

- D00: 56%
- D10: 59%
- D20: 66%
- D40: 47%

Approximate detections missed as background are:

- D00: 43%
- D10: 40%
- D20: 31%
- D40: 52%

This suggests that false negatives are currently an important
baseline limitation, particularly for D40.

Class-to-class misclassification appears relatively small compared
with missed detections.

## Confidence Threshold

The F1-confidence curve gives a maximum overall F1 of approximately
0.60 at a confidence threshold of 0.26.

Increasing the confidence threshold improves Precision but reduces
Recall. Very high thresholds therefore produce fewer false positives
but also increase missed road damage.

A threshold near 0.26 is currently a reasonable baseline candidate,
but the final operating threshold will be selected after deeper
false-positive and false-negative analysis.

## Initial Findings

1. D20 is currently the strongest class.
2. D40 is currently the weakest class.
3. Missed detections appear to be a larger issue than
   class-to-class misclassification.
4. D00 appears to generate relatively more background false positives.
5. Confidence threshold selection requires balancing false positives
   against missed damage.

## Next Steps

- Perform detailed False Positive analysis.
- Perform detailed False Negative analysis.
- Identify misclassification examples.
- Compare correct detections with failure cases.
- Investigate possible causes such as small damage, low contrast,
  lighting/shadows, road texture, camera angle, and annotation ambiguity.
- Review results.csv/results.png for training behavior.
- Propose targeted improvement experiments based on observed errors.

## Interpretation and Improvement Direction

The baseline results indicate that the model is generally able to
distinguish between the four road-damage classes when a damage instance
is detected. However, missed detections remain a major limitation,
especially for D40.

## Based on the current evidence, the next improvement stage should focus on:

- Investigating why D40 has a higher missed-detection rate.
- Reviewing validation images for small, distant, low-contrast, or
  partially visible road damage.
- Investigating false-positive D00 predictions on background regions.
- Testing confidence-threshold settings around the current F1 optimum
  rather than selecting a very high threshold based only on Precision.
- Considering targeted augmentation or class-imbalance treatment only
  after the FP/FN analysis confirms that these changes are justified.

No model-improvement experiment will be selected using the held-out
test set. Validation data will be used for experiment selection, while
the test set will remain reserved for final evaluation.