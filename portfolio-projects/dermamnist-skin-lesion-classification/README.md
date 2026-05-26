# DermaMNIST Skin Lesion Classification

Deep learning comparison for multiclass skin lesion classification on DermaMNIST.

**Authors:** Patricia Rodrigo Barrio and Victor Rodriguez Albendea

## Overview

In this academic project, we have compared several deep learning strategies for multiclass skin lesion classification using DermaMNIST. Our work evaluates a custom CNN trained from scratch, ImageNet transfer learning, radiology-domain transfer learning and a dermatology-oriented pretrained reference model.

We have focused on comparing model behavior under class imbalance, using robust metrics such as Macro F1 and Balanced Accuracy alongside Accuracy, Cohen's Kappa and Macro Recall.

## Dataset

We use DermaMNIST, a MedMNIST subset derived from HAM10000.

- 7 skin lesion classes.
- Official train, validation and test splits.
- RGB images resized to 224 x 224.

Raw DermaMNIST data and clinical images are not redistributed in this repository. To reproduce the work, the dataset must be obtained through MedMNIST or the corresponding official sources.

## Models Compared

- M1: custom CNN trained from scratch.
- M2: ResNet50 ImageNet with shallow tuning.
- M3: ResNet50 ImageNet with partial deep tuning.
- M4: ResNet50 RadImageNet/RAC with shallow tuning.
- M5: ResNet50 RadImageNet/RAC with partial deep tuning.
- M6: EfficientNet-B1 / MaxNet dermatology-oriented reference model with frozen backbone.

## Methodology

We have evaluated the models using the official test split and bootstrap-based uncertainty estimates. The comparison prioritizes metrics that are more informative under class imbalance:

- Accuracy
- Balanced Accuracy
- Macro F1
- Macro Recall
- Cohen's Kappa
- Training time

We also include selected aggregate figures for model comparison and learning-curve interpretation.

## Main Results

The main comparative conclusion of our work is that M3, the ImageNet-pretrained ResNet50 with partial deep tuning, achieved the best comparable Macro F1 and Balanced Accuracy. M6 achieved the highest Accuracy and Kappa, but did not outperform M3 in Macro F1.

For detailed metric values, see `docs/RESULTS_SUMMARY.md` and the JSON files under `results/metrics/`.

## Figures

The public repository includes only final aggregate figures:

- `figures/final_metrics_comparison.png`
- `figures/macro_f1_vs_training_time.png`
- `figures/m3_learning_curves.png`

Complete raw image galleries, clinical examples and full Grad-CAM galleries are not included.

## Repository Structure

```text
.
|-- docs/
|   |-- LICENSING.md
|   |-- RESULTS_SUMMARY.md
|   |-- WEIGHTS.md
|   `-- dermamnist_skin_lesion_classification_report.pdf
|-- figures/
|   |-- final_metrics_comparison.png
|   |-- macro_f1_vs_training_time.png
|   `-- m3_learning_curves.png
|-- models/
|   `-- checkpoints/
|       `-- .gitkeep
|-- notebooks/
|   `-- dermamnist_skin_lesion_classification.ipynb
|-- results/
|   `-- metrics/
|-- scripts/
|   |-- inspect_results.py
|   `-- make_paper_figures.py
|-- .gitignore
|-- LICENSE
|-- README.md
`-- requirements.txt
```

## Checkpoints and Weights

We do not redistribute full model checkpoints, trained weights or external pretrained weights in this public version. This includes TensorFlow/Keras checkpoints, PyTorch checkpoints, ImageNet-derived weights, RadImageNet/RAC resources, ISIC/MaxNet resources and any other external weight files.

See `docs/WEIGHTS.md` for details.

## How to Reproduce

1. Create a Python environment.
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Download DermaMNIST through MedMNIST or the official source.
4. Obtain any external pretrained weights from their original providers, respecting their licenses.
5. Open the notebook:

```bash
jupyter notebook notebooks/dermamnist_skin_lesion_classification.ipynb
```

The notebook was originally developed in Google Colab with GPU acceleration. Local reproduction may require adapting paths for datasets, caches and external weights.

## Publication Notes

This public repository includes code, documentation, aggregate metrics and final figures. It excludes:

- raw datasets and clinical images;
- complete Grad-CAM galleries;
- model checkpoints and trained weights;
- external pretrained weights;
- logs, caches and compressed data files;
- private local paths, tokens and credentials.

