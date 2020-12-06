import math 

def get_boarding_passes():
    boarding_passes = []
    with open("input.txt", "r") as f:
        while True:
            line = f.readline()
            if line:
                line = line.strip()
                line = line.replace("\n","")
                boarding_passes.append(line)
            else:
                break
    return boarding_passes

def get_row(boarding_passes):
    row_max = 127
    row_min = 0
    row = -1
    for char in boarding_passes[:7]:
        if char == 'B':
            row_min = math.ceil((row_max+row_min)/2) 
        else:
            row_max = math.floor((row_max+row_min)/2)
    row = row_min
    return row

def get_column(boarding_passes):
    row_max = 7
    row_min = 0
    row = -1
    for char in boarding_passes[7:]:
        if char == 'R':
            row_min = math.ceil((row_max+row_min)/2) 
        elif char == 'L':
            row_max = math.floor((row_max+row_min)/2)
    row = row_min
    return row

def get_seat_id(row,column):
    return row*8 + column
if __name__ == "__main__":
    bp = get_boarding_passes()
    '''
    #make sure with known input
    #check row
    print(get_row("FBFBBFFRLR") == 44) 
    print(get_row("BFFFBBFRRR") == 70)
    print(get_row("FFFBBBFRRR") == 14) 
    print(get_row("BBFFBBFRLL") == 102) 
    #check column
    print(get_column("FBFBBFFRLR") == 5) 
    print(get_column("BFFFBBFRRR") == 7)
    print(get_column("FFFBBBFRRR") == 7) 
    print(get_column("BBFFBBFRLL") == 4)
    #check seat id
    print(get_seat_id(44,5) == 357)
    print(get_seat_id(70,7) == 567)
    print(get_seat_id(14,7) == 119)
    print(get_seat_id(102,4) == 820)
    '''
    full_seat_info = {}
    highest_seat_id = 0
    hsi = [] #highest seat info
    lowest_sid = -12
    lsi = [] #lowest seat info
    for b in bp:
        row = get_row(b)
        column = get_column(b)
        sid = get_seat_id(row,column)
        if row not in full_seat_info:
            full_seat_info[row] = []
        full_seat_info[row].append(column)
        if sid > highest_seat_id:
            highest_seat_id = sid
            hsi = (row, column, sid)
        elif sid < lowest_sid or lowest_sid == -12:
            lowest_sid = sid
            lsi = (row, column, sid)
    print("SID IS NUMBER TO THE FAR RIGHT")
    print("HIGHEST SID", hsi)
    print("LOWEST SID", lsi)
    #sort full seat info
    for col in full_seat_info.keys():
        full_seat_info[col].sort()
        if len(full_seat_info[col]) != 8 and col != lsi[0] and col != hsi[0]:
            print("MISSING SEAT COLUMN", col, full_seat_info[col])
            for num in range(7):
                if full_seat_info[col][num] != num:
                    print("ID OF MISSING SEAT", get_seat_id(col, num)) 
                #check for edge case of number is 7
                if 7 not in full_seat_info[col]:
                    print("ID OF MISSING SEAT", get_seat_id(col, 7))
                    break