with open("input.txt", "r") as f:
    done = False
    valid = 0
    invalid = 0
    while done == False: #this loop is for the entire file
        passport = ""
        done = False
        while True: #this loop is for each passport
            line = f.readline()
            if line:
                if line == "\n":
                    break
                passport += line.replace("\n"," ")
            else:
                done = True
                break
        passport.strip()
        #check if correct nunber of inputs or one less without country code
        print(passport, end = '|')
        passport = passport.split(" ")
        if passport[len(passport)-1] == "":
            passport.pop(len(passport)-1)
        print(len(passport), end="|")
        has_cid = False
        has_byr = False
        has_eyr = False
        has_hgt = False
        has_hcl = False
        has_ecl = False
        has_pid = False
        has_iyr = False
        for item in passport:
            if "cid" in item:
                has_cid = True
            if "eyr" in item:
                item = item.split(":")[1]
                if int(item) <= 2030 and int(item) >= 2020:
                    has_eyr =True
            if "byr" in item:
                item = item.split(":")[1]
                if int(item) <= 2002 and int(item) >= 1920:
                    has_byr = True
            if "hgt" in item:
                item = item.split(":")[1]
                if "cm" in item:
                    item = item.split("cm")[0]
                    if int(item) <= 193 and int(item) >= 150:
                        has_hgt = True
                if "in" in item:
                    item = item.split("in")[0]
                    if int(item) <= 76 and int(item) >= 59:
                        has_hgt = True
            if "hcl" in item:
                item = item.split(":")[1]
                if len(item) == 7 and item[0] == "#":
                    has_hcl = True
            if "ecl" in item:
                item = item.split(":")[1]
                if item in "amb blu brn gry grn hzl oth":
                    has_ecl = True
            if "pid" in item:
                item = item.split(":")[1]
                if len(item) == 9 and item.isnumeric():
                    has_pid = True
            if "iyr" in item:
                item = item.split(":")[1]
                if int(item) <= 2020 and int(item) >= 2010:
                    has_iyr = True
        if has_byr and has_eyr and has_hgt and has_hcl and has_ecl and has_pid and has_iyr:
            print("valid")
            valid += 1
        else:
            print("INVLAID")
            invalid += 1
    print("----------")
    print("invalid", invalid)
    print("valid", valid)
    