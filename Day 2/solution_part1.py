#solution 1
good = 0
bad = 0
with open("input.txt") as f:
    while True:
        line = f.readline()
        if line:
            min_max,char,string = line.split(" ")
            min_max = min_max.split("-")
            char = char.replace(":","")
            count = 0
            for c in string:
                if c == char: 
                    count += 1
            if count >= int(min_max[0]) and count <= int(min_max[1]):
                good += 1
            else:
                bad += 1
        else:
            break
    print("total", good+bad)
    print("bad", bad)
    print("good", good)