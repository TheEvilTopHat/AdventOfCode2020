"""
code for day 7 
https://adventofcode.com/2020/day/7

lots of fun recursion
"""

def get_statments():
    statments = {} #bag: [(number, bag),] <- bag: contains
    with open("input.txt", "r") as f:
        while True:
            line = f.readline()
            if line:
                line = line.replace("bags","bag")
                bag, contains = line.split(" contain ")
                statments[bag] = []
                contains = contains.split(",")
                for contain in contains:
                    contain = contain.replace(".","")
                    contain = contain.strip()
                    contain = contain.lstrip()
                    if "no other bag" in contain:
                        number = 0
                        bag_type = "none"
                    else:
                        number = int(contain[0])
                        bag_type = contain[1:]
                        bag_type = bag_type.lstrip()
                    statments[bag].append((number,bag_type))
            else:
                break
    return statments

def get_combinations(statements, scopy, current_bag):
    scopy = scopy.copy() #list of keys
    number = 0
    for contain in statements[current_bag]:
        if contain[1] in scopy and contain[1] != current_bag: 
            if contain[0] == 0:
                return 0
            elif contain[1] == "shiny gold bag":
                return 1
            else:
                bag = contain[1]
                scopy.remove(contain[1])
                number += get_combinations(statements,scopy,bag) 
    return number

def get_number_of_bags_in_bag(statements, scopy, current_bag):
    if statements[current_bag][0][0] == 0:
        return 0
    number = 0
    for contain in statements[current_bag]:
        n = contain[0]
        bag = contain[1]
        for i in range(n):
            number += 1 #add one for each bag 
            number += get_number_of_bags_in_bag(statements,scopy,bag) #add how many bags in bag
    return number


if __name__ == "__main__":
    statements = get_statments()
    number = 0
    for bag in statements.keys():
        if get_combinations(statements, set(statements.keys()), bag) >= 1:
            number += 1
    print("number of bags that will hold a gold bag", number)
    print("how many bags in the gold bag", get_number_of_bags_in_bag(statements, set(statements.keys()), "shiny gold bag"))