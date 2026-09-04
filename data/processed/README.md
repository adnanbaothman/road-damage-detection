# Processed RDD2022 Dataset

This folder documents the processed YOLO-format RDD2022 dataset used for training and evaluation.

## Dataset Structure

rdd2022_yolo/
├── data.yaml
├── train/
│   ├── images/
│   └── labels/
├── val/
│   ├── images/
│   └── labels/
└── test/
    ├── images/
    └── labels/

## Split Sizes

- Train: 30,707 images
- Validation: 3,833 images
- Test: 3,845 images

The existing split must be reused for all experiments.

## Download Processed Dataset

[rdd2022_yolo.zip](https://drive.google.com/file/d/11p897gkikbXYE1rLKsJE_hfDNXmzJxl4/view?usp=sharing)

## Related Files

Split manifest:
data/eda/rdd2022_split_manifest.csv

EDA files:
data/eda/

## Important

Do not create a new train/validation/test split for model experiments.

Use the provided split to keep all experiments directly comparable with the baseline.
