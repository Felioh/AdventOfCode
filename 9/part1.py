import parse
import numpy as np

def follow(x, y):
    dx1 = x[0] - y[0]
    dx2 = x[1] - y[1]

    if abs(dx1) > 1:
        x = (x[0] - (dx1 - 1 * np.sign(dx1)), y[1])
    elif abs(dx2) > 1:
        x = (y[0], x[1] - (dx2 - 1 * np.sign(dx2)))
    return x

def main():
    with open("/mnt/c/Users/felix/workspace/adventOfCode/9/in.txt", "r") as f:
        moves = parse.findall("{:l} {:d}", f.read())
    
    all_pos = set()
    pos_h = (0, 0)
    pos_t = (0, 0)
    for m in moves:
        for s in range(m[1]):
            if m[0] == "D":
                pos_h = (pos_h[0], pos_h[1] - 1)
            elif m[0] == "U":
                pos_h = (pos_h[0], pos_h[1] + 1)
            elif m[0] == "R":
                pos_h = (pos_h[0] + 1, pos_h[1])
            elif m[0] == "L":
                pos_h = (pos_h[0] - 1, pos_h[1])
        
            pos_t = follow(pos_t, pos_h)
            all_pos.add(pos_t)
        # print(m[0], m[1], "         ", pos_h, pos_t)
        # print(all_pos)
        # input()
    print(len(all_pos))
if __name__ == "__main__":
    main()