import numpy as np
import pandas as pd
import parse

res = 0

def evaluate(c, v):
    global res
    if (c-20) % 40 == 0:
        res += (c * v)
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
            
    print(res)
if __name__ == '__main__':
    main()