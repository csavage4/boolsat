#!/usr/bin/python

def parseCNFFile(file):
    clauses = []
    vars_keys = set()
    with open(file, 'r') as input_file:
        for line in input_file:
            parsed = line.split()
            if not parsed or parsed[0] == 'p' or parsed[0] == 'c':
                continue
            else:
                eff_parsed = parsed[:-1]
                clause = set()
                for literal in eff_parsed:
                    literal = int(literal)
                    clause.add(literal)
                    vars_keys.add(abs(literal))
                clauses.append(list(clause))
    vars = dict.fromkeys(vars_keys, False)
    return clauses, vars