import numpy as np

def visible(x, y, v, trees):
    return all(val < v for val in trees[:x, y]) or \
           all(val < v for val in trees[x+1:, y]) or \
           all(val < v for val in trees[x, :y]) or \
           all(val < v for val in trees[x, y+1:])
    
def main():
    trees = np.genfromtxt("8/in.txt", dtype=int, delimiter=1)
    
    n_visible = [True for (x, y), tree in np.ndenumerate(trees) if visible(x, y, tree, trees)]
    print(len(n_visible))
        
if __name__ == "__main__":
    main()