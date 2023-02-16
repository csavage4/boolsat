#!/usr/bin/python

import sys
import time
from pathlib import Path
from dimacs_parser import parseCNFFile
from dpll import dpll


def main(argv):
    
    if(len(argv) < 2):
        print("Usage: python Main.py <cnf file>")
        return
    file_path = argv[1]
    filename = Path(file_path).name
    
    start = time.time()
    clauses, vars = parseCNFFile(file_path)
    sol = dpll(vars, clauses)
    end = time.time()
    
    if sol is False:
        ans = '{"Instance": "' + filename + '", "Time": %.2f' %(end-start) + ', "Result": "UNSAT"}'
        print(ans)
    else:
        not_first = False
        ans = '{"Instance": "' + filename + '", "Time": %.2f' %(end-start) + ', "Result": "SAT", "Solution": "'
        for k, v in sol.items():
            if not_first:
                ans += ' '
            else:
                not_first = True
            if v:
                ans += str(k) + ' true'
            else:
                ans += str(k) + ' false'
        ans += '"}'
        print(ans)


if __name__ == '__main__':
    main(sys.argv)
