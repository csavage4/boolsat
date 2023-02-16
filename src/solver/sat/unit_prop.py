#!/usr/bin/python

from update_clause import update_clauses


def unit_prop(vars, clauses):
    unit_var = set()
    for clause in clauses:
        if len(clause) == 1:
            unit_var.add(clause[0])
    while len(unit_var) > 0:
        for unit in unit_var:
            vars, clauses = update_clauses(vars, unit, clauses)
        unit_var = set()
        vars, clauses = unit_prop(vars, clauses)
    return vars, clauses