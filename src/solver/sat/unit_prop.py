#!/usr/bin/python

from update_clause import update_clauses


def unit_prop(vars, clauses, ple_vals, tot_nums):
    unit_var = set()
    for clause in clauses:
        if len(clause) == 1:
            unit_var.add(clause[0])
    while len(unit_var) > 0:
        for unit in unit_var:
            vars, clauses, ple_vals, tot_nums = update_clauses(vars, unit, clauses, ple_vals, tot_nums)
        unit_var = set()
        vars, clauses, ple_vals, tot_nums = unit_prop(vars, clauses, ple_vals, tot_nums)
    return vars, clauses, ple_vals, tot_nums