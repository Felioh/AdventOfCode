import numpy as np
    
def visible(x, y, v, trees):
    dirs = [reversed(trees[:x, y]), trees[x+1:, y], reversed(trees[x, :y]), trees[x, y+1:]]
    score = np.zeros(4, dtype=int)
    for s in range(0, 4):
        for i in dirs[s]:
            score[s] = score[s]+1
            if i >= v:
                break
            
    return np.prod(score)
    
def main():
    trees = np.genfromtxt("8/in.txt", dtype=int, delimiter=1)
    
    n_visible = [visible(x, y, tree, trees) for (x, y), tree in np.ndenumerate(trees)]
    print(max(n_visible))
        
if __name__ == "__main__":
    main()