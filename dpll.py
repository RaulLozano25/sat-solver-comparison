import random

_strategy = "first"

def set_strategy(name):
    global _strategy
    _strategy = name

def choose_variable(clauses):
    variables = list({abs(l) for c in clauses for l in c})
    if _strategy == "random":
        return random.choice(variables)
    elif _strategy == "jw":
        scores = {}
        for clause in clauses:
            for lit in clause:
                var = abs(lit)
                scores[var] = scores.get(var, 0) + 2 ** (-len(clause))
        return max(scores, key=scores.get)
    elif _strategy == "mom":
        min_len = min(len(c) for c in clauses)
        shortest = [c for c in clauses if len(c) == min_len]
        freq = {}
        for clause in shortest:
            for lit in clause:
                var = abs(lit)
                freq[var] = freq.get(var, 0) + 1
        return max(freq, key=freq.get)
    else:  # default to "first"
        return variables[0]

def unit_propagate(clauses, assignment):
    changed = True
    while changed:
        changed = False
        unit_clauses = [c for c in clauses if len(c) == 1]
        for unit in unit_clauses:
            lit = unit[0]
            if lit in assignment or -lit in assignment:
                continue
            assignment.add(lit)
            new_clauses = []
            for c in clauses:
                if lit in c:
                    continue
                new_clause = [x for x in c if x != -lit]
                new_clauses.append(new_clause)
            clauses = new_clauses
            changed = True
    return clauses, assignment

def dpll(clauses, assignment=None):
    if assignment is None:
        assignment = set()

    clauses, assignment = unit_propagate(clauses, assignment)

    if [] in clauses:
        return False
    if not clauses:
        return True

    variable = choose_variable(clauses)

    for val in [variable, -variable]:
        new_assignment = assignment.copy()
        new_assignment.add(val)
        new_clauses = []
        for clause in clauses:
            if val in clause:
                continue
            new_clause = [l for l in clause if l != -val]
            new_clauses.append(new_clause)
        if dpll(new_clauses, new_assignment):
            return True

    return False
