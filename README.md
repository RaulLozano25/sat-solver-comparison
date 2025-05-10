# SAT Solver Comparison

This project contains a theoretical and experimental comparison of three SAT solving algorithms:
- Resolution
- Davis–Putnam (DP)
- DPLL with multiple heuristics (First, Random, MOM, Jeroslow–Wang)

## 📂 Structure

- `main.py` – Runs all solvers on a predefined set of CNF instances and prints results.
- `dpll.py` – DPLL implementation with support for multiple decision heuristics.
- `dp.py` – Davis–Putnam solver (variable elimination).
- `resolution.py` – Resolution-based solver for detecting unsatisfiability.

## 🧪 CNF Instances

All CNF formulas are hardcoded inside `main.py` for clarity and reproducibility.  
Each instance is tested across all solvers to compare satisfiability detection and execution time.

## 🧠 Heuristics Implemented

In `dpll.py`, the solver supports the following decision strategies:
- First unassigned variable
- Random selection
- MOM's heuristic
- Jeroslow–Wang heuristic

## ▶️ How to run

Make sure you have Python 3.x installed. Then run:

```bash
python main.py
