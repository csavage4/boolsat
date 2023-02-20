#!/usr/bin/python

import copy
from ple import ple
from update_clause import update_clauses
from unit_prop import unit_prop
from heuristic_split import var_split


def dpll(vars, clauses, ple_vals, tot_nums):
    vars, clauses, ple_vals, tot_nums = ple(vars, clauses, ple_vals, tot_nums)
    vars, clauses, ple_vals, tot_nums = unit_prop(vars, clauses, ple_vals, tot_nums)
    if [] in clauses:
        return False
    if len(clauses) == 0:
        return vars
    split_var = var_split(clauses)
    tmp = copy.deepcopy(clauses)
    tmp_var, tmp_cl, tmp_ple, tmp_nums = update_clauses(vars, split_var, clauses, ple_vals, tot_nums)
    assignment = dpll(tmp_var, tmp_cl, tmp_ple, tmp_nums)
    if assignment is False:
        clauses = copy.deepcopy(tmp)
        tmp_var, tmp_cl, tmp_ple, tmp_nums = update_clauses(vars, -split_var, clauses, ple_vals, tot_nums)
        assignment = dpll(tmp_var, tmp_cl, tmp_ple, tmp_nums)
        if assignment is False:
            return False
    return assignment