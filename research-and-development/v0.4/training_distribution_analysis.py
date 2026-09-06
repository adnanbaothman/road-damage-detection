from pathlib import Path
from collections import Counter

label_dir = Path(
    "/Users/abdullah/road-damage-data/rdd2022_yolo/train/labels"
)

class_names = {
    0: "D00",
    1: "D10",
    2: "D20",
    3: "D40"
}

counts = Counter()
total_images = 0
d40_images = 0

for label in label_dir.glob("*.txt"):
    total_images += 1
    has_d40 = False

    for line in label.read_text().splitlines():
        parts = line.split()

        if not parts:
            continue

        class_id = int(float(parts[0]))
        counts[class_id] += 1

        if class_id == 3:
            has_d40 = True

    if has_d40:
        d40_images += 1


print("\nTraining class distribution:")

for class_id in range(4):
    print(
        f"{class_names[class_id]}: "
        f"{counts[class_id]} instances"
    )

print("\nTotal instances:", sum(counts.values()))
print("Training images:", total_images)
print("Images containing D40:", d40_images)
print(
    "D40 image percentage:",
    round(d40_images / total_images * 100, 2),
    "%"
)