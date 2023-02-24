#!/usr/bin/python

import copy
from ple import ple
from update_clause import update_clauses
from unit_prop import unit_prop
from heuristic_split import var_split

def dpll(vars, clauses, ple_vals, tot_nums, J):
    vars, clauses, ple_vals, tot_nums, kinda_new_j = ple(vars, clauses, ple_vals, tot_nums, J)
    vars, clauses, ple_vals, tot_nums, sorta_new_j = unit_prop(vars, clauses, ple_vals, tot_nums, kinda_new_j)
    if [] in clauses:
        return False
    if len(clauses) == 0:
        return vars
    split_var = var_split(sorta_new_j)
    tmp = copy.deepcopy(clauses)
    tmp_var, tmp_cl, tmp_ple, tmp_nums, tmp_newnewj = update_clauses(vars, split_var, clauses, ple_vals, tot_nums, sorta_new_j)
    assignment = dpll(tmp_var, tmp_cl, tmp_ple, tmp_nums, tmp_newnewj)
    if assignment is False:
        tmp_var, tmp_cl, tmp_ple, tmp_nums, tmp_newnewj = update_clauses(vars, -split_var, tmp, ple_vals, tot_nums, sorta_new_j)
        assignment = dpll(tmp_var, tmp_cl, tmp_ple, tmp_nums, tmp_newnewj)
        if assignment is False:
            return False
    return assignment