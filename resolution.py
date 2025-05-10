def resolve(ci, cj):
    resolvents = []
    for li in ci:
        for lj in cj:
            if li == -lj:
                new_clause = list(set(ci + cj))
                new_clause.remove(li)
                new_clause.remove(lj)
                resolvents.append(new_clause)
    return resolvents

def resolution(clauses):
    new = set()
    while True:
        pairs = [(clauses[i], clauses[j]) for i in range(len(clauses))
                 for j in range(i + 1, len(clauses))]
        for (ci, cj) in pairs:
            resolvents = resolve(ci, cj)
            for r in resolvents:
                if r == []:
                    return False  # contradiction ⇒ UNSAT
                new.add(tuple(sorted(r)))
        new_clauses = [list(c) for c in new if list(c) not in clauses]
        if not new_clauses:
            return True  # no new clauses ⇒ SAT
        clauses.extend(new_clauses)
