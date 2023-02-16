#!/usr/bin/python
def update_clauses(vars, variable, clauses):
    upd_clauses = []
    if variable >= 0:
        vars[variable] = True
    else:
        vars[abs(variable)] = False
    for clause in clauses:
        if variable in clause:
            continue
        else:
            if -variable in clause:
                clause.remove(-variable)
            upd_clauses.append(clause)
    return vars, upd_clauses