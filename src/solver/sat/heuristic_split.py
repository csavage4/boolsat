#!/usr/bin/python

import random
from collections import defaultdict


def var_split(J):
    var_pair = [-1, 0]
    keys = list(J.keys())
    for k in keys:
        tot = J[k] + J[-k]
        if tot > var_pair[1] and var_pair[0] != -k:
            var_pair = [k, tot]

    split = abs(var_pair[0])
    

    if J[split] >= J[-split]:
        return split
    else:
        return -split