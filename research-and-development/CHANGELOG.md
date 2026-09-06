# R&D Changelog

## v0.3 - 2026-09-06

- Added manual field-testing observations from the RoadGuard AI Streamlit prototype.
- Documented dark-mode visibility issue in the Detected Objects panel.
- Documented a suspected single-detection behavior on images containing more than one damaged area; this requires controlled verification to separate model behavior from UI rendering behavior.
- Documented reduced detection reliability on visually complex and low-light scenes.
- Added four screenshots as qualitative evidence.
- Added a prioritized R&D plan for UI correction, multi-damage testing, difficult-scene testing, and D40-focused model improvement.

## v0.2

- Reproduced full validation on all 3,833 validation images.
- Recorded overall and per-class precision, recall, mAP50, and mAP50-95.
- Added automated FP/FN analysis at confidence threshold 0.26 and IoU threshold 0.50.
- Identified D40 as the weakest class, mainly because of missed detections.

## v0.1

- Replaced the generic `yolov8n.pt` model in the prototype with the project-trained `best.pt` model.
- Added reliable RGB input conversion.
- Set the prototype inference confidence threshold to 0.26.
- Confirmed the prototype can detect Road Damage classes D00, D10, D20, and D40 instead of generic COCO objects.
