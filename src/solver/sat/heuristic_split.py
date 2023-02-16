#!/usr/bin/python

import random
from collections import defaultdict


def var_split(clauses):
    J = defaultdict(int)
    for clause in clauses:
        clause_len = len(clause)
        for lit in clause:
            J[lit] += 2 ** (-clause_len)

    choices = []
    vals = []
    for k in J.keys():
        lit = abs(k)
        if lit not in choices:
            choices.append(lit)
            if -k in J:
                vals.append(J[k] + J[-k])
            else:
                vals.append(J[k])

    split = random.choices(choices, weights=vals, k=1)
    split = split[0]

    split = random.choices([split, -split], weights=[J[split], J[-split]], k=1)
    split = split[0]
    return split