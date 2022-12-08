import numpy as np

def visible(x, y, v, trees):
    if x <= 0 or v > max(trees[:x, y]):
        return True
    elif x >= len(trees) - 1 or v > max(trees[x+1:, y]):
        return True
    elif y <= 0 or v > max(trees[x, :y]):
        return True
    elif y >= len(trees[x]) - 1 or v > max(trees[x, y+1:]):
        return True
    return False
    
def main():
    trees = np.genfromtxt("8/in.txt", dtype=int, delimiter=1)
    
    n_visible = [True for (x, y), tree in np.ndenumerate(trees) if visible(x, y, tree, trees)]
    print(len(n_visible))
        
if __name__ == "__main__":
    main()