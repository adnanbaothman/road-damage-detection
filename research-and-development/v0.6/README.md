# RoadGuard AI R&D v0.6

## Improved Model Evaluation

Version 0.6 evaluates the improved RoadGuard AI model after D40-focused
oversampling and continued YOLO11s training.

## Main Changes

- D40 training images were oversampled 2x.
- Training entries increased from 30,707 to 33,645.
- Validation and test sets were not modified.
- YOLO11s training was completed to 50 epochs.
- The improved model is stored at:

`reports/improved/weights/roadguard_best.pt`

## Final Validation Results

| Metric | Result |
|---|---:|
| Precision | 0.662 |
| Recall | 0.553 |
| mAP50 | 0.607 |
| mAP50-95 | 0.322 |

## D40 Results

| Metric | Result |
|---|---:|
| Precision | 0.609 |
| Recall | 0.492 |
| mAP50 | 0.528 |
| mAP50-95 | 0.253 |

## Field Testing

The improved model successfully detected multiple D40 road-damage areas
in Saudi road images where the previous baseline model produced no detections.

Some difficult scenes are still missed, especially unusual viewpoints,
rotated images, distant damage, and complex Saudi road environments.

## Conclusion

The D40-focused experiment improved detection performance, but further
Saudi-specific training data is required for stronger real-world
generalization.