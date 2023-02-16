#!/usr/bin/python

import copy
from ple import ple
from update_clause import update_clauses
from unit_prop import unit_prop
from heuristic_split import var_split


def dpll(vars, clauses):
    vars, clauses = ple(vars, clauses)
    vars, clauses = unit_prop(vars, clauses)
    if [] in clauses:
        return False
    if len(clauses) == 0:
        return vars
    split_var = var_split(clauses)
    tmp = copy.deepcopy(clauses)
    tmp_var, tmp_cl = update_clauses(vars, split_var, clauses)
    assignment = dpll(tmp_var, tmp_cl)
    if assignment is False:
        clauses = copy.deepcopy(tmp)
        tmp_var, tmp_cl = update_clauses(vars, -split_var, clauses)
        assignment = dpll(tmp_var, tmp_cl)
        if assignment is False:
            return False
    return assignment