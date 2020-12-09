import itertools

#invalid number from step one 530627549

def get_numbers():
    nums = []
    with open("input.txt", "r") as f:
        while True:
            line = f.readline()
            if line:
                line = line.strip()
                line = line.lstrip()
                nums.append(int(line))
            else:
                break
    return nums

def generate_comb(nums,start,end):
    comb_add = []
    for comb in itertools.combinations(nums[start:end],2):
        comb_add.append(sum(comb))
    return set(comb_add)

def find_contiguois_sets(nums, number):
    for l in range(2,1000): #size of the lists to genearte the sets
        for i in range(len(nums)):
            if i+l > len(nums):
                break
            comb = nums[i:i+l]
            comb_set = set(comb)
            if len(comb_set) >= 2:
                if sum(comb_set) == number:
                    small_big = min(list(comb_set)) + max(list(comb_set))
                    return (small_big, sum(comb_set), comb_set, comb)
    return False


if __name__ == "__main__":
    nums = get_numbers()
    # find the first number that does not have two numbers in 
    # the last 25 numbers added together equal it
    invalid_num = -1
    combs = generate_comb(nums, 0,25)
    i = 0
    for num in nums[25:]:
        i += 1
        if num not in combs:
            invalid_num = num
            break
        combs = generate_comb(nums, i,i+25)
    print("INVALID NUM", invalid_num)
    # find a contiguous set of at least two numbers 
    # in your list which sum to the invalid number from step 1
    print("CON SET", find_contiguois_sets(nums,invalid_num))