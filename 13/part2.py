import numpy as np
import pandas as pd
import parse


def compare(l, r):
    if type(l) == int and type(r) == int:
        return l - r
    if type(l) == int or type(r) == int:  # basically xor
        return compare([l] if isinstance(l, int) else l, [r] if isinstance(r, int) else r)

    ziplr = zip(l, r)
    for i, (l1, r1) in enumerate(ziplr):
        diff = compare(l1, r1)
        if diff != 0:
            return diff

    return len(l) - len(r)


def main():
    with open('/mnt/c/Users/felix/workspace/adventOfCode/13/in.txt') as f:
        pairs = f.read().split("\n\n")
    div1, div2 = 2, 6
    i1 = 1
    i2 = 2  # because of div1..
    for pair in pairs:
        ppairs = pair.split("\n")
        for ppair in ppairs:
            if compare(eval(ppair), div1) < 0:
                i1 += 1
            if compare(eval(ppair), div2) < 0:
                i2 += 1
    print(i1*i2)


if __name__ == '__main__':
    main()
