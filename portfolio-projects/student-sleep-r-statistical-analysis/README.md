# Student Sleep and Wellbeing Statistical Analysis in R

Completed master's coursework project · R Programming & Statistical Analysis

## Overview

This R Markdown project studies the relationship between sleep habits, emotional wellbeing and academic performance in university students. The analysis includes data cleaning, imputation, exploratory analysis, hypothesis testing, transformations, regression modeling and diagnostic checks.

## Dataset Description

The dataset contains university student information related to sleep habits, chronotype, GPA, missed classes, cognition score, sleep quality, depression, anxiety, stress, happiness, alcohol use, weekday and weekend sleep patterns, and all-nighter status.

The dataset was provided for academic coursework. Because explicit permission to publish the raw data has not been confirmed, the raw text file is not included in the clean repository structure. See `data/README.md` for local reproduction instructions.

## Research Questions

- Is average sleep duration related to academic performance?
- Are depression, anxiety and stress associated with poorer sleep quality?
- Does chronotype relate to sleep quality or cognitive performance?
- Are early classes associated with lower weekday sleep duration?

## Data Preprocessing

The workflow defines variable types, checks constant and near-constant variables, identifies anomalous or inconsistent values, analyzes missingness and applies multiple imputation using `mice`.

## Statistical Methodology

- Exploratory analysis
- Missing value analysis
- Multiple imputation using `mice`
- Shapiro-Wilk normality testing
- Box-Cox transformations
- Pearson correlation
- Multiple linear regression
- Regression residual diagnostics
- Kruskal-Wallis test
- ANOVA
- Levene test
- Wilcoxon / Mann-Whitney test
- Visual reporting with `ggplot2` and base R plots

## Main Conclusions

The following conclusions are supported by the R Markdown report:

- Average sleep hours were not significantly related to GPA.
- Depression and anxiety were associated with poorer sleep quality, while stress was not significant in the reported multiple regression model.
- Chronotype showed significant differences in sleep quality.
- Chronotype was not significantly associated with cognitive performance.
- Early classes were not significantly associated with lower weekday sleep duration.

## Repository Structure

```text
.
|-- analysis/
|   `-- student_sleep_analysis.Rmd
|-- data/
|   `-- README.md
|-- figures/
|-- report/
|   `-- student_sleep_statistical_analysis.pdf
|-- .gitignore
|-- portfolio_entry.json
|-- README.md
`-- requirements.R
```

## How to Reproduce

1. Install the required R packages listed below. You can also run:

```r
source("requirements.R")
```

2. Place the local dataset at:

```text
data/Grupo4_Sueno.txt
```

3. Render the R Markdown file:

```r
rmarkdown::render("analysis/student_sleep_analysis.Rmd")
```

TODO: The copied R Markdown references `UPV_LOGO.png` in the header, but that image was not present in the inspected folder. Add the logo locally or remove the include line before rendering.

## R Packages Used

`flextable`, `knitr`, `clickR`, `mice`, `ggplot2`, `reshape2`, `car`, `MASS`, `gridExtra` and `scales`.

## Group Project Note

This was completed as a master's coursework group project. This repository is prepared as a professional portfolio version of the work while keeping coursework data publication constraints explicit.
