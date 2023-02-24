#!/usr/bin/python
def update_clauses(vars, variable, clauses, ple_vals, tot_nums, J):
    upd_clauses = []
    if variable >= 0:
        vars[variable] = True
    else:
        vars[abs(variable)] = False
    for clause in clauses:
        leng = len(clause)
        if variable in clause:
            for literal in clause:
                ple_vals[abs(literal)]-=(int(variable/abs(variable)))
                tot_nums[abs(literal)]-=1
                x=2**(-leng)
                if literal in J.keys() and J[literal]>=x:
                    J[literal] -= 2**(-leng)
            continue
        else:
            if -variable in clause:
                clause.remove(-variable)
                ple_vals[abs(variable)]-=(int(variable/abs(variable)))
                tot_nums[abs(variable)]-=1
                for literal in clause:
                    J[literal] += 2**(-leng)
            upd_clauses.append(clause)
    if variable in J.keys():   
        del J[variable]
    if -variable in J.keys():   
        del J[-variable]
    return vars, upd_clauses, ple_vals, tot_nums, J