# RoadGuard AI R&D v0.3 - Field Testing and Interface Findings

## Purpose

Document qualitative issues observed while manually testing the current baseline in the RoadGuard AI Streamlit interface. These observations complement the formal validation and FP/FN analysis; they do not replace those metrics.

## Finding 1 - Dark-mode result visibility issue

### Observation

In light mode, the Detected Objects result card is readable. In dark mode, the result area can appear blank or unreadable even when a D40 detection is visible on the image.

### Interpretation

This is most likely an interface/CSS contrast issue rather than a model issue. The model prediction can still be present while the text in the result card is not visible.

### Action

Review the Streamlit CSS for result-card background and text colors under both themes. Use theme-aware colors or explicit high-contrast text/background rules.

## Finding 2 - Suspected single-detection behavior on multi-damage images

### Observation

During manual testing, some images appear to contain more than one damaged region, but the prototype shows only one detection.

### Important qualification

This observation alone does not prove that the model "ignores" the other damage. The cause could be:

1. the model produced only one box,
2. another box was below the confidence threshold,
3. Non-Maximum Suppression removed an overlapping box,
4. the UI code is rendering/listing only one of several model outputs.

### Verification plan

For a controlled multi-damage test set, compare:

```python
len(results[0].boxes)
```

with the number of boxes and rows displayed in the UI. If the raw model has multiple boxes but the UI shows one, it is an application bug. If the raw model also returns one, it is a model/inference issue.

## Finding 3 - Difficult scenes reduce detection reliability

### Observation

The model is less reliable when the road image contains many visual details, low-light conditions, vehicles, reflections, complex textures, distance, or small damage regions. One tested night scene returned no objects detected.

### Interpretation

This is consistent with the previously measured false-negative/recall weakness. The current evidence suggests the next model-improvement work should include hard examples, especially for D40 and small/low-contrast damage.

### Action

Create a hard-case evaluation bucket with tags such as:

- night/low light
- cluttered scene
- small damage
- distant damage
- wet/reflection
- low contrast
- multiple damages

Use the same hard-case images before and after retraining to measure qualitative improvement.

## Screenshot observations

### Figure A - Light mode, successful D40 detection

`assets/light_mode_d40_071.jpg`

The model detects D40 at approximately 0.71 confidence and the Detected Objects card is readable in light mode.

### Figure B - Dark mode, low-confidence D40 detection

`assets/dark_mode_d40_029.jpg`

The model detects D40 at approximately 0.29 confidence in a visually busy road scene. The result panel visibility should be checked separately from detection quality.

### Figure C - Dark mode, stronger D40 detection with blank result card

`assets/dark_mode_d40_071.jpg`

The image shows a D40 detection at approximately 0.71 confidence, while the Detected Objects card appears blank/unreadable. This is strong qualitative evidence for the dark-mode UI issue.

### Figure D - Complex night scene with no detection

`assets/complex_night_scene_no_detection.jpg`

The road scene contains low light, reflections, vehicles, and complex textures. The prototype reports no objects detected. This is a useful hard-case example for future before/after testing.

## Priority order

1. Verify whether multi-damage behavior is a model issue or UI-output issue.
2. Improve D40 and hard-case recall using controlled retraining.
3. Fix dark-mode result-card visibility independently in the Streamlit UI.
4. Re-test the same Saudi field images against the improved model.

## Acceptance criteria for the next version

- Detected Objects content is readable in both light and dark mode.
- Every raw YOLO prediction returned by the model can be displayed/listed by the UI.
- D40 Recall improves above the current 0.439 baseline without a major precision loss.
- D40 mAP50 improves above 0.520.
- Difficult-scene test images show measurable improvement or clearly documented remaining limitations.
