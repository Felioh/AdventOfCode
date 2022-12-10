import numpy as np
import pandas as pd
import parse

def evaluate(c, v, res=[]): #using the mutability of lists
    res.append((".", "#")[abs((c % 40) - v) < 2])

    if len(res) % 40 == 0:
        print(' '.join(res[-40:]))
    return c + 1

def main():
    with open('/mnt/c/Users/felix/workspace/adventOfCode/10/in.txt') as f:
        content = f.readlines()
    cycles = 0
    X = 1
    for l in content:
        if l.startswith("noop"):
            cycles = evaluate(cycles, X)
        else:
            for i in range(2):
                cycles = evaluate(cycles, X)
            X += parse.parse("addx {:d}\n", l)[0]

if __name__ == '__main__':
    main()