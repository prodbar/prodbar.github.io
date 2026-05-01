# Next Steps

## What Changed

### healthcare-cost-multivariate-analysis

- Added a professional `README.md`.
- Added `portfolio_entry.json`.
- Added `requirements.txt`.
- Added `.gitignore`.
- Created `notebooks/` with clean notebook copies:
  - `pca_regression_lda.ipynb`
  - `mca_analysis.ipynb`
  - `mca_clustering.ipynb`
- Created `report/healthcare_cost_multivariate_analysis.pdf`.
- Created `data/README.md` explaining how to obtain the Kaggle dataset.
- Left the original coursework files in place locally and ignored them for future commits.

### production-scheduling-optimization

- Added a professional `README.md`.
- Added `portfolio_entry.json`.
- Added `requirements.txt`.
- Added `.gitignore`.
- Created `src/` with clean script copies:
  - `01_generate_data.py`
  - `02_extensions.py`
- Created `data/generated/` with generated CSV extension inputs.
- Created `excel/` with clean Excel/OpenSolver workbook copies.
- Created `report/` with the final report and execution instructions.
- Created `results/` with computational results and checkpoint output.
- Left the original coursework folder in place locally and ignored it for future commits.

### student-sleep-r-statistical-analysis

- Added a professional `README.md`.
- Added `portfolio_entry.json`.
- Added `.gitignore`.
- Created `analysis/student_sleep_analysis.Rmd` as a clean copy.
- Updated the copied R Markdown dataset path to `../data/Grupo4_Sueno.txt`.
- Created `report/student_sleep_statistical_analysis.pdf`.
- Created `data/README.md` explaining that the coursework dataset is not included.
- Left the original coursework files and dataset in place locally and ignored them for future commits.

## Files to Review Manually

- `healthcare-cost-multivariate-analysis/notebooks/*.ipynb`: confirm paths work after downloading the Kaggle dataset.
- `healthcare-cost-multivariate-analysis/report/healthcare_cost_multivariate_analysis.pdf`: confirm the report is the final version intended for public sharing.
- `production-scheduling-optimization/src/01_generate_data.py`: update the hardcoded Excel path before rerunning.
- `production-scheduling-optimization/src/02_extensions.py`: update the hardcoded Excel path before rerunning.
- `production-scheduling-optimization/report/*.pdf`: confirm these are the final public versions.
- `student-sleep-r-statistical-analysis/analysis/student_sleep_analysis.Rmd`: add `UPV_LOGO.png` locally or remove the logo include before rendering.
- `student-sleep-r-statistical-analysis/report/student_sleep_statistical_analysis.pdf`: confirm the report is appropriate for public sharing.

## Files Not to Commit if Data Publication Is Uncertain

- `healthcare-cost-multivariate-analysis/medical_insurance.csv`
- `healthcare-cost-multivariate-analysis/data/*.csv`
- `student-sleep-r-statistical-analysis/Grupo4_Sueño.txt`
- `student-sleep-r-statistical-analysis/Grupo4_Sueno.txt`
- `student-sleep-r-statistical-analysis/data/Grupo4_Sueño.txt`
- `student-sleep-r-statistical-analysis/data/Grupo4_Sueno.txt`

## Suggested GitHub Repository Names

- `healthcare-cost-multivariate-analysis`
- `production-scheduling-optimization`
- `student-sleep-r-statistical-analysis`

## Suggested Git Commands

Run these from each project folder after reviewing the files. Do not run `git push` until the remote repository exists and the public-sharing review is complete.

### healthcare-cost-multivariate-analysis

```bash
cd healthcare-cost-multivariate-analysis
git init
git add .
git status
git commit -m "Prepare portfolio-ready healthcare cost analysis project"
git branch -M main
git remote add origin https://github.com/prodbar/healthcare-cost-multivariate-analysis.git
```

### production-scheduling-optimization

```bash
cd production-scheduling-optimization
git init
git add .
git status
git commit -m "Prepare portfolio-ready scheduling optimization project"
git branch -M main
git remote add origin https://github.com/prodbar/production-scheduling-optimization.git
```

### student-sleep-r-statistical-analysis

```bash
cd student-sleep-r-statistical-analysis
git init
git add .
git status
git commit -m "Prepare portfolio-ready student sleep analysis project"
git branch -M main
git remote add origin https://github.com/prodbar/student-sleep-r-statistical-analysis.git
```

## Portfolio Integration

- Use `portfolio_projects_entries.json` as the source for copying the three project entries into the main portfolio later.
- Add GitHub repository links to each `portfolio_entry.json` only after the repositories are created.
