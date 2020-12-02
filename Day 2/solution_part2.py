good = 0
bad = 0
with open("input.txt") as f:
    while True:
        line = f.readline()
        if line:
            min_max,char,string = line.split(" ")
            min_max = min_max.split("-")
            char = char.replace(":","")
            single = False
            for c in range(len(string)):
                if string[c] == char and str(c+1) in min_max:
                    if single:
                        single = False
                    else:
                        single = True
            if single:
                good += 1
            else:
                bad += 1
        else:
            break
    print("total", good+bad)
    print("bad", bad)
    print("good", good)