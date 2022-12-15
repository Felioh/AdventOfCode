import numpy as np
import pandas as pd
import parse

def main():
    with open("/mnt/c/Users/felix/workspace/adventOfCode/15/in.txt", "r") as f:
        lines = f.readlines()
    sensors = parse.findall("Sensor at x={sx:d}, y={sy:d}: closest beacon is at x={bx:d}, y={by:d}", str(lines))
    
    sens = []
    for s in sensors:
        dist = abs(s["sx"] - s["bx"]) + abs(s["sy"] - s["by"]) #simplified distance..
        sens.append((s["sx"], s["sy"], dist, s["bx"], s["by"]))

    skip = {}
    for x in range(4000000):
        if str(x) in skip.keys():
            x = skip[str(x)]
            skip = {str(x+1):x-1}
        y = 0
        while y <= 4000000:
            notCovered = True
            for s in sens:
                dist = abs(x - s[0]) + abs(y -s[1])
                if dist <= s[2]:
                    y_n = s[1] + (dist - abs(s[0]-x))
                    skip[str(y+1)] = y_n-1
                    y = y_n
                    notCovered = False
                    break
            if notCovered:
                print(x, y, x* 4000000 + y)
            y += 1
    
if __name__ == '__main__':
    main()