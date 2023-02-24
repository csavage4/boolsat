#!/usr/bin/python

from update_clause import update_clauses


def unit_prop(vars, clauses, ple_vals, tot_nums, J):
    new_j = J
    unit_var = set()
    for clause in clauses:
        if len(clause) == 1:
            unit_var.add(clause[0])
    if len(unit_var) > 0:
        for unit in unit_var:
            vars, clauses, ple_vals, tot_nums, new_j = update_clauses(vars, unit, clauses, ple_vals, tot_nums, new_j)
        vars, clauses, ple_vals, tot_nums, new_j = unit_prop(vars, clauses, ple_vals, tot_nums,new_j)
    return vars, clauses, ple_vals, tot_nums, new_j