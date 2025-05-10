def eliminate_var(clauses, var):
    pos = [c for c in clauses if var in c]
    neg = [c for c in clauses if -var in c]
    new_clauses = []

    for p in pos:
        for n in neg:
            resolvent = list(set([l for l in p if l != var] + [l for l in n if l != -var]))
            new_clauses.append(resolvent)

    remaining = [c for c in clauses if var not in c and -var not in c]
    return remaining + new_clauses

def dp(clauses, variables):
    if [] in clauses:
        return False
    if not clauses:
        return True
    if not variables:
        return True  # SAT (no variables left and no contradictions)

    var = variables[0]
    new_clauses = eliminate_var(clauses, var)
    return dp(new_clauses, variables[1:])
