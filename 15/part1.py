import numpy as np
import pandas as pd
import parse

y = 2000000

def main():
    with open("/mnt/c/Users/felix/workspace/adventOfCode/15/in.txt", "r") as f:
        lines = f.readlines()
    sensors = parse.findall("Sensor at x={sx:d}, y={sy:d}: closest beacon is at x={bx:d}, y={by:d}", str(lines))
    
    cirles = []
    beacons = []
    max_x = 0
    min_x = 0
    for s in sensors:
        dist = abs(s["sx"] - s["bx"]) + abs(s["sy"] - s["by"]) #simplified distance..
        cirles.append((s["sx"], s["sy"], dist))
        beacons.append(((s["bx"], s["by"])))
        max_x = max(s["sx"] + dist, max_x)
        min_x = min(s["sx"] - dist, min_x)
    
    res = 0
    for i in range(min_x, max_x):
        for c in cirles:
            dist = abs(c[0] - i) + abs(c[1] - y) #simplified distance..
            if dist <= c[2] and (i, y) not in beacons:
                res += 1
                break
    print(res)
    
if __name__ == '__main__':
    main()