import numpy as np
    
def visible(x, y, v, trees):
    l, r, u, d = 0, 0, 0, 0
    for i in reversed(trees[:x, y]):
        l = l+1
        if i >= v:
            break
    for i in trees[x+1:, y]:
        r = r+1
        if i >= v:
            break
    for i in reversed(trees[x, :y]):
        u = u+1
        if i >= v:
            break
    for i in trees[x, y+1:]:
        d = d+1
        if i >= v:
            break
    return l*r*u*d
    
def main():
    trees = np.genfromtxt("8/in.txt", dtype=int, delimiter=1)
    
    n_visible = [visible(x, y, tree, trees) for (x, y), tree in np.ndenumerate(trees)]
    print(max(n_visible))
        
if __name__ == "__main__":
    main()