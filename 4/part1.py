import numpy as np

def main():
    data = np.loadtxt("in.txt", dtype=str)
    
    nb_dubs = 0
    for row in data:
        ranges = row.split(',')
        borders1 = ranges[0].split('-')
        borders2 = ranges[1].split('-')
        if int(borders1[0]) <= int(borders2[0]) and int(borders1[1]) >= int(borders2[1]):
            nb_dubs = nb_dubs + 1
        elif int(borders1[0]) >= int(borders2[0]) and int(borders1[1]) <= int(borders2[1]):
            nb_dubs = nb_dubs + 1

        # print(borders1, borders2)

        # exit()
    print(nb_dubs)

if __name__ == "__main__":
    main()