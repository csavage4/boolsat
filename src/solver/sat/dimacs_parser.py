#!/usr/bin/python

from collections import defaultdict

def parseCNFFile(file):
    clauses = []
    vars_keys = set()
    ple_vals = defaultdict(int)
    tot_nums = defaultdict(int)
    J = defaultdict(int)
    with open(file, 'r') as input_file:
        for line in input_file:
            parsed = line.split()
            if not parsed or parsed[0] == 'p' or parsed[0] == 'c':
                continue
            else:
                eff_parsed = parsed[:-1]
                clause = set()
                leng = len(eff_parsed)
                for literal in eff_parsed:
                    literal = int(literal)
                    clause.add(literal)
                    vars_keys.add(abs(literal))
                    ple_vals[abs(literal)]+=int(literal/abs(literal))
                    tot_nums[abs(literal)]+=1
                    J[literal] += (2 **(-leng))

                clauses.append(list(clause))
    vars = dict.fromkeys(vars_keys, False)
    return clauses, vars, ple_vals, tot_nums, J