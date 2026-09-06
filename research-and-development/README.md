# RoadGuard AI - Research & Development

This folder records the technical research, evaluation, field-testing observations, and model-improvement decisions for the RoadGuard AI capstone project.

The documentation is versioned so the team can see how the project evolved from baseline integration to quantitative error analysis and then to real-world interface/model testing.

## Version history

- `v0.1` - Baseline integration and validation
- `v0.2` - Full validation and FP/FN error analysis
- `v0.3` - Field testing, UI findings, model limitations, and next R&D plan

## Current status

The current baseline is a trained YOLO11s road-damage detector loaded from `reports/baseline/weights/best.pt` and used by the Streamlit prototype. The formal validation set contains 3,833 images. The current improvement priority is D40 recall and difficult-scene robustness, while a separate UI fix is needed for dark-mode result visibility.

## Important rule for experiments

Keep the validation and test splits unchanged. New training experiments should be compared against the same baseline so improvements are measurable and fair.

## Current report

See `v0.3/reports/RoadGuard_AI_RnD_Report_v0.3.pdf` for the cumulative R&D report with screenshots.
