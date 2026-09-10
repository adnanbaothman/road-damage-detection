# Saudi Domain Adaptation Plan

## Objective

Improve detection performance on Saudi road environments.

## Data Needed

Collect images containing:

- Potholes
- Longitudinal cracks
- Transverse cracks
- Alligator cracks
- Patched roads
- Sand and dust
- Construction roads
- Bright sunlight
- Shadows
- Different camera angles
- Near and distant road damage

## Labels

- D00
- D10
- D20
- D40

## Training Strategy

Use the v0.6 improved model as the starting checkpoint and fine-tune it
with a mixed dataset containing RDD2022 and labeled Saudi road images.

## Evaluation

Compare precision, recall, mAP50, mAP50-95, and Saudi field-test results.