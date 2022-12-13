import numpy as np
import pandas as pd
import parse


def compare(l, r):
    if type(l) == int and type(r) == int:
        return l - r
    if type(l) == int or type(r) == int:  # basically xor
        return compare([l] if isinstance(l, int) else l, [r] if isinstance(r, int) else r)

    ziplr = zip(l, r)
    for _, (l1, r1) in enumerate(ziplr):
        diff = compare(l1, r1)
        if diff != 0:
            return diff

    return len(l) - len(r)


def main():
    with open('/mnt/c/Users/felix/workspace/adventOfCode/13/in.txt') as f:
        pairs = f.read().split("\n\n")

    res = sum([i+1 for i in range(len(pairs))
              if compare(eval(pairs[i].split("\n")[0]), eval(pairs[i].split("\n")[1])) < 0])

    print(res)


if __name__ == '__main__':
    main()
