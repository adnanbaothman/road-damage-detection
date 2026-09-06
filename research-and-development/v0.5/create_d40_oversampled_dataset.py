from pathlib import Path
import argparse


CLASS_NAMES = {
    0: "D00",
    1: "D10",
    2: "D20",
    3: "D40",
}


def contains_d40(label_path):
    if not label_path.exists():
        return False

    for line in label_path.read_text().splitlines():
        parts = line.strip().split()

        if parts and int(float(parts[0])) == 3:
            return True

    return False


def main():
    parser = argparse.ArgumentParser(
        description="Create a 2x D40 oversampled training manifest."
    )

    parser.add_argument(
        "--dataset-root",
        required=True,
        help="Path to the RDD2022 YOLO dataset",
    )

    args = parser.parse_args()

    dataset_root = Path(args.dataset_root).resolve()

    image_dir = dataset_root / "train" / "images"
    label_dir = dataset_root / "train" / "labels"

    output_manifest = dataset_root / "train_d40_2x.txt"
    output_yaml = dataset_root / "data_d40_2x.yaml"

    image_extensions = {
        ".jpg",
        ".jpeg",
        ".png",
    }

    images = sorted(
        image
        for image in image_dir.iterdir()
        if image.suffix.lower() in image_extensions
    )

    manifest = []

    d40_images = 0

    for image in images:
        label = label_dir / f"{image.stem}.txt"

        # Every training image appears once.
        manifest.append(str(image.resolve()))

        # D40-containing images appear one additional time.
        if contains_d40(label):
            d40_images += 1
            manifest.append(str(image.resolve()))

    output_manifest.write_text(
        "\n".join(manifest) + "\n"
    )

    yaml_content = f"""path: {dataset_root}

train: {output_manifest}
val: val/images
test: test/images

names:
  0: D00
  1: D10
  2: D20
  3: D40
"""

    output_yaml.write_text(yaml_content)

    print("\n====================================")
    print("D40 OVERSAMPLING PREPARATION COMPLETE")
    print("====================================")

    print(f"Original training images: {len(images)}")
    print(f"Images containing D40:   {d40_images}")
    print(f"Training entries after oversampling: {len(manifest)}")

    print("\nGenerated:")
    print(output_manifest)
    print(output_yaml)

    print("\nValidation and test sets were NOT modified.")


if __name__ == "__main__":
    main()