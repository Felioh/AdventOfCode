import numpy as np

def main():
    with open("in.txt") as f:
        data = np.loadtxt((x.replace('-', ',') for x in f), dtype=int, delimiter=',')

    nb_overlaps = len([True for row in data if range(max(row[0], row[2]), min(row[1], row[3])+1)])

    print(nb_overlaps)

if __name__ == "__main__":
    main()