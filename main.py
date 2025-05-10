import time
from copy import deepcopy
from resolution import resolution
from dp import dp
from dpll import dpll, set_strategy

def get_instances():

    return [
        ("SAT - Trivial", [[1], [2], [3]], [1, 2, 3]),
        ("SAT - Moderate", [[1, -2], [-1, 3], [-3, 4], [2, -4]], [1, 2, 3, 4]),
        ("UNSAT - Simple", [[1], [-1]], [1]),
        ("UNSAT - Complex", [[1, 2], [-1, 2], [1, -2], [-1, -2]], [1, 2]),
        ("SAT - Heuristic Test", [[1, 2, 3], [1, -2], [1, -3], [-1, 2], [-1, -2]], [1, 2, 3])
    ]

def run_solver(name, func, *args):
    start = time.perf_counter()
    result = func(*args)
    end = time.perf_counter()
    elapsed = (end - start) * 1000
    return f"{name:<20} | Result: {'SAT' if result else 'UNSAT':<6} | Time: {elapsed:.4f} ms"

def main():
    strategies = ["first", "random", "jw", "mom"]

    print("\n--- SAT Solver Comparative Analysis ---\n")

    for title, clauses, variables in get_instances():
        print(f"\nInstance: {title}\n")

        print(run_solver("Resolution", resolution, deepcopy(clauses)))
        print(run_solver("Davis–Putnam", dp, deepcopy(clauses), variables))

        for strat in strategies:
            set_strategy(strat)
            label = f"DPLL ({strat})"
            print(run_solver(label, dpll, deepcopy(clauses)))

if __name__ == "__main__":
    main()
