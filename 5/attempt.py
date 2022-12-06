import numpy as np
import parse

def parse_moves(instr):
    return parse.findall("move {num} from {src} to {dest}", instr)

def parse_state(instr):
    stacks = list(list())
    num_stacks = int((len(instr[-1]) / 4))
    for stack in range(0, num_stacks):
        stacks.append(list())
        for l in instr:
            c = l[(stack + 1) * 4 - 3]
            if c == ' ':
                continue
            if str(c).isnumeric():
                break
            stacks[stack].append(c)
    print(instr, len(instr[-1]))
    return stacks

def main():
    with open("/mnt/c/Users/felix/workspace/adventOfCode/5/in.txt", "r") as f:
        lines = f.readlines()
    state = parse_state(lines[:9])
    moves = parse_moves(str(lines[9:]))
    for m in moves:
        num_el = int(m["num"])
        els = state[int(m["src"])-1][:num_el]
        state[int(m["src"])-1] = state[int(m["src"])-1][num_el:]
        els.extend(state[int(m["dest"])-1])
        state[int(m["dest"])-1] = els
        print("take 1 from ", m["src"], "to", m["dest"], els)
    for stack in state:
        print(stack[0])
    input()

if __name__ == "__main__":
    main()