import numpy as np

def main():
    data = np.loadtxt("in.txt", dtype=str)
    
    prio_sum = 0
    for i in range(0, len(data), 3):
        ks1 = data[i]
        ks2 = data[i + 1]
        ks3 = data[i + 2]

        # print(ks)
        # print(p1, " ", p2)
        for c in ks1:
            if c in ks2 and c in ks3:
                # print(c)
                if ord(c) >= 97:
                    prio_sum += ord(c) - 96
                    break
                else:
                    prio_sum += ord(c) - 38
                    break
                print("WARN!!")
        # exit()
    print(prio_sum)
if __name__ == "__main__":
    main()