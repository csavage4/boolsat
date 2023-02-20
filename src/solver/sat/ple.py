#!/usr/bin/python

from update_clause import update_clauses


def ple(vars, clauses, ple_vals, tot_nums):
    for i in ple_vals.keys():
        if(abs(ple_vals[i])==tot_nums[i] & tot_nums[i]!=0):
            vars, clauses, ple_vals, tot_nums = update_clauses(vars, i*int((abs(ple_vals[i])/ple_vals[i])), clauses, ple_vals, tot_nums)
    return vars, clauses, ple_vals, tot_nums