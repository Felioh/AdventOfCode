import numpy as np

def main():
    data = np.loadtxt("in.txt", dtype=str)
    
    prio_sum = 0
    for ks in data:
        h = (int) (len(ks) / 2)
        p1 = ks[:h]
        p2 = ks[h:]
        # print(ks)
        # print(p1, " ", p2)
        for c in p1:
            if c in p2:
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