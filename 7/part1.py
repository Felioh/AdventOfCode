
dirs = dict()

current_dirs = list()

def main():
    res = 0
    with open("7/in.txt", "r") as f:
        lines = f.read().split("\n")
    
    for l in lines:
        if l[0] == "$":
            if l[2] == "c":
                if l[5:] == "..":
                    d = current_dirs.pop()
                    # if dirs[d] <= 100000:
                    #     res += dirs[d]
                else:
                    if l[5:] not in dirs.keys():
                        dirs[l[5:]] = 0
                    current_dirs.append(l[5:])
        elif l.startswith("dir "):
            continue
        else:
            parts = l.split(" ")
            for d in current_dirs:
                try:
                    dirs[d] = dirs[d] + int(parts[0])
                except KeyError:
                    dirs[d] = int(parts[0])
            # print(dirs)
            # input()
    for v in dirs.values():
        if v <= 100000:
            res += v
    print(res)
if __name__ == "__main__":
    main()