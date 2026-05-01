# Gen Z Mental Wellness Multivariate Monitoring

## Overview

This project analyses the Gen Z Mental Wellness dataset from a multivariate perspective, combining exploratory, predictive and classification-oriented methods. The work studies how lifestyle habits, digital exposure and psychological wellbeing variables relate to anxiety and burnout risk in a young population.

## Dataset

The analysis is based on the Gen Z Mental Wellness dataset. After preprocessing and sample selection, the final working sample contains 2,064 observations.

The study is organized into two analytical blocks:

- Lifestyle and digital habits, used to explore and predict `Anxiety_Score`.
- Psychological wellbeing variables, used to analyze and classify `Burnout_Risk`.

The raw Excel dataset is kept local unless publication permission is confirmed.

## Methodology

The project combines:

- PCA to explore latent structures and variable relationships.
- Hotelling's T2 and SPE statistics for multivariate diagnostic analysis.
- MLR, PCR and PLS to model `Anxiety_Score` from lifestyle and digital habit variables.
- PLS-DA to discriminate burnout risk from psychological variables.
- Random Forest as a nonlinear predictive benchmark.
- Cross-validation to support model selection.
- Confusion matrices, ROC curves and classification metrics for model assessment.

## Main Findings

- The first PCA block revealed a dominant digital exposure axis mainly associated with social media use and screen time.
- Additional latent components captured secondary structures related to sleep, night scrolling and online gaming.
- `Anxiety_Score` was mainly associated with lower sleep duration, higher night scrolling and greater digital exposure.
- PLS provided the most interpretable latent structure for explaining anxiety, despite similar predictive performance to MLR and PCR.
- In the psychological block, PCA revealed a dominant wellbeing-versus-distress axis.
- PLS-DA showed that burnout risk discrimination was mainly driven by anxiety, emotional fatigue, motivation, sleep quality, mood stability and wellbeing.
- Random Forest achieved stronger predictive performance, while PLS-DA offered better interpretability through latent variables.

## Tools

- Python
- Dragonet
- PCA
- PLS
- PCR
- PLS-DA
- Random Forest
- Hotelling's T2
- SPE diagnostics
- Cross-validation
- Data visualization

## Repository Structure

```text
.
|-- data/
|   |-- GenZ_dataset_con_low.xlsx
|   `-- README.md
|-- notebooks/
|   `-- Codigos trabajo MOD.ipynb
|-- report/
|   `-- TRABAJO MOD - Patricia Rodrigo y Victor Rodriguez.pdf
|-- portfolio_entry.json
|-- README.md
`-- requirements.txt
```

- `notebooks/`: analysis notebook.
- `report/`: final coursework report.
- `data/`: local dataset folder.
- `portfolio_entry.json`: structured metadata for the portfolio website.

## Notes

The dataset is kept local unless publication permission is confirmed. The public portfolio should not publish raw data without explicit confirmation.
