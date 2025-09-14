'''
Implement few list operations.

1. Find a value. Just return True or False if the value is found.
2. Get the index of the value if the value is found else -1.
3. Get the number of occurances of the value in the list. for e.g., if the list has the number `2` 10 times, then return 10. If the value is not found, return `0`
'''

import random
from time import perf_counter

def contains(nums, to_find):

    for num in nums:
        if num == to_find:
            return True # return right away.
    
    return False

def builtin_contains(nums, to_find):
    if to_find in nums:
        return True
    else:
        return False

    # return to_find in nums


def index_of(nums, to_find):

    index = -1
    for num in nums:
        index += 1
        if num == to_find:
            return index
    return -1

def builtin_index(nums, to_find):
    if builtin_contains(nums, to_find):
        return nums.index(to_find)
    else:
        return -1


def count_occurances(nums, to_find):
    '''
    Returns the number of occurances in the list.
    '''

    num_of_items = 0

    for num in nums:
        if num == to_find:
            num_of_items += 1
    
    return num_of_items


def count_occurances_v2(nums, to_find):
    '''
    Returns the number of occurances in the list.
    Assume the list is sorted.
    '''

    num_of_items = 0

    for num in nums:
        if num == to_find:
            num_of_items += 1        
        elif num > to_find:
            return num_of_items
        
    
    return num_of_items




def builtin_count(nums, to_find):
    return nums.count(to_find)

# **** Perf test *** #

def test_custom_count(nums, to_find, repeat):
    start = perf_counter()
    num_of_occurances = 0
    for _ in range(0, repeat):
        num_of_occurances = count_occurances(nums, to_find)
    
    end = perf_counter()

    print(f"[test custom count]     => {to_find} is found {num_of_occurances} times in the list. Time taken: {(end - start):.6f}s")


def test_custom_count_v2(nums, to_find, repeat):
    start = perf_counter()
    num_of_occurances = 0
    sorted_list = sorted(nums)
    for _ in range(0, repeat):
        num_of_occurances = count_occurances_v2(sorted_list, to_find)
    
    end = perf_counter()

    print(f"[test custom count v2]  => {to_find} is found {num_of_occurances} times in the list. Time taken: {(end - start):.6f}s")




def test_builtin_count(nums, to_find, repeat):
    start = perf_counter()
    num_of_occurances = 0
    for _ in range(0, repeat):
        num_of_occurances = builtin_count(nums, to_find)
    
    end = perf_counter()

    print(f"[test builtin count]    => {to_find} is found {num_of_occurances} times in the list. Time taken: {(end - start):.6f}s")


def test_perf():
    lo = 1
    hi = 1000
    repeat = 100

    nums = []
    for _ in range(lo, hi):
        nums.append(random.randint(lo, hi))

    to_find = random.randint(lo, hi)

    test_builtin_count(nums, to_find, repeat)
    test_custom_count(nums, to_find, repeat)
    test_custom_count_v2(nums, to_find, repeat)


def main():
    nums = [1,2,3,4,5,6]
    to_find = 6

    found = contains(nums, to_find)
    print(f"[custom contains] => {to_find} is in the list: {found}")

    found = builtin_contains(nums, to_find)
    print(f"[builtin contains] => {to_find} is in the list: {found}")
    

    index = index_of(nums, to_find)
    print(f"[custom index_of] => {to_find} is at the index : {index}")

    to_find = 5
    index = index_of(nums, to_find)
    print(f"[custom index] => {to_find} is at the index : {index}")

    index = builtin_index(nums, to_find)
    print(f"[buitin index] => {to_find} is at the index : {index}")


    num_of_occurances = count_occurances(nums, to_find)
    print(f"[custom count] => {to_find} is found {num_of_occurances} times in the list")

    nums.append(5)
    print("After appending 5....")
    
    num_of_occurances = count_occurances(nums, to_find)
    print(f"[custom count] => {to_find} is found {num_of_occurances} times in the list")

    num_of_occurances = builtin_count(nums, to_find)
    print(f"[builtin count] => {to_find} is found {num_of_occurances} times in the list")


    test_perf()    





if __name__ == '__main__':
    main()