import numpy as np

def main():
    with open("1/in.txt", "r") as f:
        src = f.read()
        src = src.replace("\n", ",")
        src = src.split(",,")
        maxC = 0
        for cals in src:
            tmpC = 0
            items = cals.split(",")
            for i in items:
                tmpC += int(i)
            if tmpC > maxC and tmpC < 69249:
                maxC = tmpC
        print(maxC)
if __name__ == "__main__":
    main()
    
    
# 71300 + 69249 + 69142