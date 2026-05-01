# Healthcare Cost Analytics with Multivariate Methods

Completed master's coursework project · Healthcare Analytics

## Overview

This project applies multivariate statistical methods to annual medical insurance cost analysis. The work studies demographic, clinical, lifestyle, policy and cost-related variables using dimensionality reduction, categorical data analysis, clustering and supervised classification techniques.

## Dataset

The analysis is based on the Kaggle Medical Insurance Cost Prediction dataset:

https://www.kaggle.com/datasets/mohankrishnathalla/medical-insurance-cost-prediction

The raw dataset is not included in the clean repository structure. To reproduce the analysis, download the dataset from Kaggle and place it locally according to the notes in `data/README.md`.

## Objectives

- Understand the structure of medical insurance cost data through exploratory analysis.
- Reduce dimensionality and multicollinearity using PCA.
- Combine PCA with regression modeling to study annual medical cost.
- Explore associations among categorical personal, health and lifestyle variables using MCA.
- Identify homogeneous profiles through clustering on MCA coordinates.
- Classify insured individuals into low, medium and high annual cost groups using LDA.

## Methodology

The project combines exploratory data analysis, preprocessing, dimensionality reduction, regression, categorical data analysis, clustering and supervised classification. PCA is used to synthesize economic, contractual and clinical information into interpretable latent dimensions. MCA is used to study categorical associations, and clustering is applied to MCA coordinates to identify profile groups.

## Repository Structure

```text
.
|-- data/
|   `-- README.md
|-- notebooks/
|   |-- mca_analysis.ipynb
|   |-- mca_clustering.ipynb
|   `-- pca_regression_lda.ipynb
|-- report/
|   `-- healthcare_cost_multivariate_analysis.pdf
|-- results/
|-- .gitignore
|-- portfolio_entry.json
|-- README.md
`-- requirements.txt
```

## Main Techniques

- Principal Component Analysis (PCA)
- PCA combined with regression
- Multiple Correspondence Analysis (MCA)
- Clustering on MCA coordinates
- Linear Discriminant Analysis (LDA)
- Exploratory data analysis
- Data preprocessing and interpretation

## How to Reproduce

1. Create a Python environment.
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Download the dataset from Kaggle.
4. Place the dataset locally as described in `data/README.md`.
5. Open the notebooks in `notebooks/` and run them in the documented order.

## Key Takeaways

- The project analyzes a large healthcare insurance dataset with demographic, clinical, lifestyle, policy and cost-related variables.
- PCA is used to summarize related variables into interpretable latent dimensions.
- PCA-based regression supports the study of annual cost while reducing multicollinearity.
- MCA supports interpretation of categorical health, lifestyle and profile variables.
- MCA coordinates are used as inputs for clustering to identify homogeneous profiles.
- LDA is used to classify individuals into annual cost groups.

## Technologies

Python, pandas, NumPy, scikit-learn, prince, Matplotlib, Seaborn, SciPy and statsmodels.

## Group Project Note

This was completed as a master's coursework group project. This repository is prepared as a professional portfolio version of the work, preserving the original analysis while keeping raw data publication constraints explicit.
