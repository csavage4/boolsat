#!/usr/bin/python
def update_clauses(vars, variable, clauses, ple_vals, tot_nums):
    upd_clauses = []
    if variable >= 0:
        vars[variable] = True
    else:
        vars[abs(variable)] = False
    for clause in clauses:
        if variable in clause:
            for literal in clause:
                ple_vals[abs(literal)]-=(int(variable/abs(variable)))
                tot_nums[abs(literal)]-=1
            continue
        else:
            if -variable in clause:
                clause.remove(-variable)
                ple_vals[abs(variable)]-=(int(variable/abs(variable)))
                tot_nums[abs(variable)]-=1
            upd_clauses.append(clause)
    return vars, upd_clauses, ple_vals, tot_nums