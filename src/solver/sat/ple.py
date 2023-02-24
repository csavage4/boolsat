#!/usr/bin/python

from update_clause import update_clauses


def ple(vars, clauses, ple_vals, tot_nums, J):
    new_j = J
    for i in ple_vals.keys():
        if((abs(ple_vals[i])==tot_nums[i]) and (tot_nums[i]!=0)):
            val = i*int(abs(ple_vals[i])/ple_vals[i])
            vars, clauses, ple_vals, tot_nums, new_j = update_clauses(vars, val, clauses, ple_vals, tot_nums, new_j)
    return vars, clauses, ple_vals, tot_nums, new_j