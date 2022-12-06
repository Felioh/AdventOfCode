import numpy as np

ROCK2 = 'A'
PAPER2 = 'B'
SCISSORS2 = 'C'
LOSE = 'X'
DRAW = 'Y'
WIN = 'Z'


def main():
    data = np.loadtxt("in.txt", dtype=str)
    score = 0
    for r in data:
        myChoice = r[1]
        theirChoice = r[0]
        if myChoice == WIN:
            score += 6
            if theirChoice == ROCK2:
                score += 2
            elif theirChoice == SCISSORS2:
                score += 1
            elif theirChoice == PAPER2:
                score += 3
        elif myChoice == DRAW:
            score += 3
            if theirChoice == ROCK2:
                score += 1
            elif theirChoice == SCISSORS2:
                score += 3
            elif theirChoice == PAPER2:
                score += 2
        elif myChoice == LOSE:
            if theirChoice == ROCK2:
                score += 3
            elif theirChoice == SCISSORS2:
                score += 2
            elif theirChoice == PAPER2:
                score += 1
    print(score, "\n")    
    
if __name__ == "__main__":
    main()