import parse
import numpy as np


n_knots = 10

def follow(x, y):
    dx1, dx2 = x[0] - y[0], x[1] - y[1]
    if abs(dx1) > 1:
        x = (x[0] - (dx1 - 1 * np.sign(dx1)), y[1])
    elif abs(dx2) > 1:
        x = (y[0], x[1] - (dx2 - 1 * np.sign(dx2)))
    return x

def main():
    with open("/mnt/c/Users/felix/workspace/adventOfCode/9/in.txt", "r") as f:
        moves = parse.findall("{:l} {:d}", f.read())
    
    dirs = {'R' : (1,0), 'L' : (-1,0), 'U' : (0,1), 'D' : (0,-1)}
    all_pos = set()
    knots = [(0, 0)] * n_knots
    for m in moves:
        for s in range(m[1]):
            knots[0] = (knots[0][0] + dirs[m[0]][0], knots[0][1] + dirs[m[0]][1])

            for i in range(len(knots) - 1):
                knots[i+1] = follow(knots[i+1], knots[i])
            all_pos.add(knots[-1])
            
        # print(m[0], m[1], "         ", knots[0], knots[1])
        # print(knots)
        # print(m)
        # print(all_pos)
        # input()
        # input()
    print(len(all_pos))
if __name__ == "__main__":
    main()