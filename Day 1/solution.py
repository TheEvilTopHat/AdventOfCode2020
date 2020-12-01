"""
https://adventofcode.com/2020/day/1

takes input file in same dir

this solution gets both stars
"""

#import(s) 
from itertools import combinations

def get_data_and_form_comb(num):
    """
    Read input from input file and form each line into combinations 
    with number of values based on the input
        Input: Int
        Output: List<(int,)>
    """
    nums = [] #save all the input nums here for easy management
    #get input and put each into a 
    with open("input.txt","r") as f:
        while True:
            line = f.readline()
            if not line:
                break
            line = line.strip()
            nums.append(int(line)) #remeber to convert into int
    return combinations(nums, num) #get combinations and return

def find_2020_and_multi(combs):
    """
    See which combiantion summed == 2020 
    Then multiply the nums and return the combiantion and the answer
        Input: List<(int,)> 
        Output: (int,), int
    """
    for comb in combs:
        if sum(comb) == 2020:
            multi = 1
            for num in comb:
                multi *= num
            return comb, multi
    return -1

if __name__ == "__main__":
    #for 2 nums
    #get combinations of data
    combs = get_data_and_form_comb(2)
    #get answer
    nums, answer = find_2020_and_multi(combs)
    #show nums of solution and solution
    print("2 nums")
    print("nums", nums)
    print("answer", answer)
    print("--------------")
    #for 3 nums
    #get combinations of data
    combs = get_data_and_form_comb(3)
    #get answer
    nums, answer = find_2020_and_multi(combs)
    #show nums of solution and solution
    print("3 nums")
    print("nums", nums)
    print("answer", answer)