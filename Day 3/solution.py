"""
https://adventofcode.com/2020/day/3
Part one is stored in vars map2 and trees_hit2
"""

def get_map():
    """
    Read the input file and save it into a list called map
    Do not add new line chars
    INPUT:
        None
    OUTPUT:
        List<Char>: map 
    """
    map = []
    with open("input.txt","r") as f:
        while True:
            line = f.readline()
            if not line:
                break
            row = []
            for char in line:
                if char != '\n':
                    row.append(char)
            map.append(row)
    return map

def slide(map, x,y):
    """
    slide and calculate number of trees hit
    I commented out the part that shows your path with the map
    INPUT:
        List<Char>: map -> the map to do the calucations on
        INT: x -> how far right each step is
        INT: y -> how far down each step is
    OUPUT:
        #List<Char>: map -> map with pathed graphed
        INT: trees_hit -> number of trees hit
    """
    #current position vectors
    cur_x = 0
    cur_y = 0
    #value to return
    trees_hit = 0
    while cur_y < len(map)-1:
        #go to next layer
        cur_x += x
        cur_y += y
        #make sure that the x value is not out of bounds
        #if it is out of bands wrap back to start (pattern repeates)
        if cur_x-1 >= len(map[0])-1:
            cur_x -= len(map[0])
        #check if location is tree
        if map[cur_y][cur_x] == '#':
            trees_hit += 1
            #map[cur_y][cur_x] = 'X'
        #else:
        #    map[cur_y][cur_x] = 'O'

        #print(trees_hit)
    #return map, trees_hit
    return trees_hit

if __name__ == "__main__":
    map = get_map()
    trees_hit1 = slide(map,1,1)
    trees_hit2 = slide(map,3,1)
    trees_hit3 = slide(map,5,1)
    trees_hit5 = slide(map,7,1)
    trees_hit4 = slide(map,1,2)
    print("1")
    print("trees hit", trees_hit1)
    #part one is number 2 ONLY
    print("2")
    print("trees hit", trees_hit2)
    print("3")
    print("trees hit", trees_hit3)
    print("4")
    print("trees hit", trees_hit4)
    print("5")
    print("trees hit", trees_hit5)
    print("---------------------")
    print("trees hit multiplied", trees_hit1* trees_hit2 * trees_hit3 * trees_hit4 * trees_hit5)



