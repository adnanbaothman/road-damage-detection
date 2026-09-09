# RoadGuard AI R&D v0.7

## Saudi Domain Adaptation

Status: Planned

The goal of v0.7 is to improve RoadGuard AI performance on Saudi road
conditions by fine-tuning the current improved model using labeled Saudi
road images.

## Planned Workflow

1. Collect Saudi road images.
2. Remove unusable or duplicate images.
3. Label road damage using D00, D10, D20, and D40 classes.
4. Create train, validation, and test splits.
5. Fine-tune the v0.6 improved model.
6. Evaluate using the same benchmark metrics.
7. Compare:
   - Baseline model
   - v0.6 D40-oversampled model
   - v0.7 Saudi-adapted model

## Starting Model

`reports/improved/weights/roadguard_best.pt`

## Status

Training has not started yet.