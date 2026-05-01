# Gen Z Burnout Risk Classification with Neural Networks

Multiclass neural network classification on tabular behavioral data

## Project Overview

This project studies multiclass classification of burnout risk in Gen Z using a tabular dataset with lifestyle, digital behavior and mental wellness variables. The work compares a linear softmax baseline, shallow neural networks, hyperparameter search and deeper fully connected neural network architectures.

## Dataset

The project uses the Gen Z Mental Wellness & Digital Lifestyle Patterns dataset from Kaggle:

https://www.kaggle.com/datasets/hammadansari7/gen-z-mental-wellness-and-digital-lifestyle-patterns

The dataset contains 10,000 observations and 22 variables. The target variable is `Burnout_Risk`, with three classes: Low, Medium and High. Predictors include numerical and categorical variables related to digital lifestyle, wellbeing and personal context.

The raw Excel file is kept locally under `data/` and ignored by Git until public redistribution is explicitly confirmed.

## Objectives

- Build a reproducible supervised learning pipeline for multiclass burnout risk classification.
- Compare linear and neural network approaches on tabular behavioral data.
- Address mixed numerical and categorical predictors through preprocessing.
- Use class weighting to account for imbalance in the target classes.
- Evaluate models using global and class-wise classification metrics.
- Interpret the Low class with care because it has very low support in the test set.

## Methodology

- Stratified train-validation-test split.
- z-score normalization for numerical variables.
- One-hot encoding for categorical variables.
- Class weighting to address class imbalance.
- Linear softmax baseline.
- Shallow neural network.
- Keras Tuner Hyperband search.
- Deep fully connected neural network.
- Dropout regularization.
- Activation function comparison.
- Optimizer comparison.

## Models Compared

- Linear softmax baseline.
- Shallow neural network.
- Tuned shallow neural network selected through Keras Tuner Hyperband.
- Deep multilayer perceptron with dropout regularization.
- Variants comparing activation functions and optimizers.

## Evaluation Metrics

The project evaluates models using accuracy, class-wise precision, recall, F1-score, confusion matrix and training curves.

## Key Takeaways

- The baseline linear model reached 0.901 test accuracy.
- Keras Tuner selected a 64-unit sigmoid model with learning rate 0.01 and reached 0.996 test accuracy.
- The best final model was a deep MLP with dropout, ReLU activation and RMSprop optimizer, reaching 0.997 test accuracy.
- The Low class should be interpreted carefully because it has very low support in the test set.

## Repository Structure

```text
.
|-- data/
|   `-- README.md
|-- notebooks/
|   `-- genz_burnout_neural_network_classification.ipynb
|-- report/
|   `-- genz_burnout_neural_network_classification.pdf
|-- results/
|   `-- figures/
|-- .gitignore
|-- portfolio_entry.json
`-- README.md
```

## Technologies

Python, TensorFlow, Keras, Keras Tuner, scikit-learn, pandas, NumPy, Matplotlib and Seaborn.

## Publication Notes

This folder is prepared as a portfolio-ready repository. The dataset is public on Kaggle, but the local Excel copy is ignored for now. Before publishing, confirm whether the exact local `GenZ_dataset.xlsx` file can be redistributed or instruct users to download it directly from Kaggle.
