from pathlib import Path
from collections import defaultdict
import csv

PROJECT_ROOT = Path(__file__).resolve().parents[2]

GT_DIR = Path(
    "/Users/abdullah/road-damage-data/rdd2022_yolo/val/labels"
)

PRED_DIR = (
    PROJECT_ROOT
    / "runs"
    / "detect"
    / "reports"
    / "evaluation"
    / "error_analysis"
    / "predictions"
    / "labels"
)

OUTPUT_DIR = (
    PROJECT_ROOT
    / "reports"
    / "evaluation"
    / "error_analysis"
)

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

IOU_THRESHOLD = 0.50

CLASS_NAMES = {
    0: "D00",
    1: "D10",
    2: "D20",
    3: "D40",
}


def read_labels(path, prediction=False):
    boxes = []

    if not path.exists():
        return boxes

    with open(path, "r") as f:
        for line in f:
            parts = line.strip().split()

            if len(parts) < 5:
                continue

            cls_id = int(float(parts[0]))

            xc = float(parts[1])
            yc = float(parts[2])
            w = float(parts[3])
            h = float(parts[4])

            x1 = xc - w / 2
            y1 = yc - h / 2
            x2 = xc + w / 2
            y2 = yc + h / 2

            confidence = None

            if prediction and len(parts) >= 6:
                confidence = float(parts[5])

            boxes.append({
                "class_id": cls_id,
                "box": (x1, y1, x2, y2),
                "confidence": confidence,
            })

    return boxes


def iou(box1, box2):
    x1 = max(box1[0], box2[0])
    y1 = max(box1[1], box2[1])
    x2 = min(box1[2], box2[2])
    y2 = min(box1[3], box2[3])

    intersection = max(0, x2 - x1) * max(0, y2 - y1)

    area1 = max(0, box1[2] - box1[0]) * max(0, box1[3] - box1[1])
    area2 = max(0, box2[2] - box2[0]) * max(0, box2[3] - box2[1])

    union = area1 + area2 - intersection

    if union == 0:
        return 0

    return intersection / union


summary = defaultdict(
    lambda: {
        "TP": 0,
        "FP": 0,
        "FN": 0,
        "Misclassification": 0,
    }
)

details = []

gt_files = sorted(GT_DIR.glob("*.txt"))

print(f"Ground-truth files: {len(gt_files)}")
print(f"Prediction directory: {PRED_DIR}")
print("Starting comparison...")


for index, gt_path in enumerate(gt_files, start=1):

    pred_path = PRED_DIR / gt_path.name

    gt_boxes = read_labels(gt_path)
    pred_boxes = read_labels(pred_path, prediction=True)

    candidates = []

    for gi, gt in enumerate(gt_boxes):
        for pi, pred in enumerate(pred_boxes):
            score = iou(gt["box"], pred["box"])

            if score >= IOU_THRESHOLD:
                candidates.append((score, gi, pi))

    candidates.sort(reverse=True)

    matched_gt = set()
    matched_pred = set()

    for score, gi, pi in candidates:

        if gi in matched_gt or pi in matched_pred:
            continue

        matched_gt.add(gi)
        matched_pred.add(pi)

        gt = gt_boxes[gi]
        pred = pred_boxes[pi]

        true_class = CLASS_NAMES[gt["class_id"]]
        pred_class = CLASS_NAMES[pred["class_id"]]

        if gt["class_id"] == pred["class_id"]:

            summary[true_class]["TP"] += 1
            error_type = "TP"

        else:

            summary[true_class]["Misclassification"] += 1
            error_type = "Misclassification"

        details.append({
            "image": gt_path.stem,
            "true_class": true_class,
            "predicted_class": pred_class,
            "confidence": pred["confidence"],
            "iou": round(score, 4),
            "error_type": error_type,
        })

    # unmatched GT = False Negative
    for gi, gt in enumerate(gt_boxes):

        if gi not in matched_gt:

            true_class = CLASS_NAMES[gt["class_id"]]

            summary[true_class]["FN"] += 1

            details.append({
                "image": gt_path.stem,
                "true_class": true_class,
                "predicted_class": "None",
                "confidence": "",
                "iou": "",
                "error_type": "FN",
            })

    # unmatched prediction = False Positive
    for pi, pred in enumerate(pred_boxes):

        if pi not in matched_pred:

            pred_class = CLASS_NAMES[pred["class_id"]]

            summary[pred_class]["FP"] += 1

            details.append({
                "image": gt_path.stem,
                "true_class": "None",
                "predicted_class": pred_class,
                "confidence": pred["confidence"],
                "iou": "",
                "error_type": "FP",
            })

    if index % 500 == 0:
        print(f"Processed {index}/{len(gt_files)}")


details_file = OUTPUT_DIR / "fp_fn_results.csv"

with open(details_file, "w", newline="") as f:

    writer = csv.DictWriter(
        f,
        fieldnames=[
            "image",
            "true_class",
            "predicted_class",
            "confidence",
            "iou",
            "error_type",
        ],
    )

    writer.writeheader()
    writer.writerows(details)


summary_file = OUTPUT_DIR / "fp_fn_summary.csv"

with open(summary_file, "w", newline="") as f:

    writer = csv.writer(f)

    writer.writerow([
        "Class",
        "TP",
        "FP",
        "FN",
        "Misclassification",
    ])

    for class_name in ["D00", "D10", "D20", "D40"]:

        values = summary[class_name]

        writer.writerow([
            class_name,
            values["TP"],
            values["FP"],
            values["FN"],
            values["Misclassification"],
        ])


print("\n====================================")
print("FP/FN ANALYSIS COMPLETE")
print("====================================")

for class_name in ["D00", "D10", "D20", "D40"]:

    values = summary[class_name]

    print(
        f"{class_name}: "
        f"TP={values['TP']} | "
        f"FP={values['FP']} | "
        f"FN={values['FN']} | "
        f"Misclassification={values['Misclassification']}"
    )

print("\nResults saved to:")
print(summary_file)
print(details_file)