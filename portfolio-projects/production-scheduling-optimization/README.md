# Production Scheduling Optimization on Unrelated Parallel Machines

Completed master's coursework project · Operations Research & Scheduling

## Overview

This project studies production scheduling on unrelated parallel machines under progressively more realistic constraints. It compares an Excel/OpenSolver exact base model, a Google OR-Tools CP-SAT model, a Genetic Algorithm and an Iterated Greedy metaheuristic.

## Problem Formulation

The base problem is unrelated parallel machine scheduling with makespan minimization:

```text
R || Cmax
```

The base instance contains 50 jobs and 5 unrelated parallel machines. Processing times depend on the selected machine, each job must be assigned to exactly one machine, and the objective is to minimize makespan.

## Base Model

The base exact model was implemented in Excel/OpenSolver and used as a benchmark reference for the Python-based methods. The original and executed Excel workbooks are stored in `excel/`.

## Extensions

- Extension 0: base `R || Cmax`
- Extension 1: release dates `rj`
- Extension 2: sequence-dependent setup times `sijk`
- Extension 3: precedence constraints
- Extension 4: personnel/resource availability constraints
- Extension 5: weighted tardiness objective `sum(wj Tj)`

## Solution Methods

- Excel/OpenSolver exact base model
- Google OR-Tools CP-SAT exact/constraint programming model
- Genetic Algorithm
- Iterated Greedy
- Relative Percentage Deviation (RPD) comparison

## Repository Structure

```text
.
|-- data/
|   `-- generated/
|-- excel/
|   |-- base_R_Cmax.xlsx
|   |-- executed_R_Cmax.xlsx
|   `-- original_unmodified_R_Cmax.xlsx
|-- report/
|   |-- execution_instructions.pdf
|   `-- production_scheduling_optimization.pdf
|-- results/
|   |-- checkpoint.json
|   `-- computational_results.txt
|-- src/
|   |-- 01_generate_data.py
|   `-- 02_extensions.py
|-- .gitignore
|-- portfolio_entry.json
|-- README.md
`-- requirements.txt
```

## How to Run

1. Create a Python environment.
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Review `report/execution_instructions.pdf`.
4. Update the Excel path variables in `src/01_generate_data.py` and `src/02_extensions.py` if needed.
5. Generate extension data:

```bash
python src/01_generate_data.py
```

6. Run the optimization and comparison methods:

```bash
python src/02_extensions.py
```

## Results Summary

The available computational results show that Iterated Greedy produced the best reported solution in each extension. The reported best objective values were:

- Extension 0: `Cmax = 168.00`
- Extension 1: `Cmax = 169.00`
- Extension 2: `Cmax = 195.00`
- Extension 3: `Cmax = 197.00`
- Extension 4: `Cmax = 199.00`
- Extension 5: `sum(wjTj) = 3060.00`

The full method comparison, timings, RPD values and machine sequences are stored in `results/computational_results.txt`.

## Technologies

Python, Google OR-Tools, CP-SAT, Genetic Algorithm, Iterated Greedy, Excel, OpenSolver, NumPy and openpyxl.

## Group Project Note

This was completed as a master's coursework group project. This repository is prepared as a professional portfolio version of the work, with original coursework folders preserved locally and clean copies placed in publication-ready locations.
