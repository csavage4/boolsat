#!/usr/bin/python

from update_clause import update_clauses


def ple(vars, clauses):
    pur = set()
    vr = 0
    negation = 0
    other_literals = set()
    for clause in clauses:
        for literal in clause:
            vr = abs(literal)
            negation = -literal
            if negation not in pur:
                if vr not in other_literals:
                    pur.add(literal)
            else:
                pur.remove(negation)
                other_literals.add(vr)
    
    for literal in pur:
        vars, clauses = update_clauses(vars, literal, clauses)
    return vars, clauses