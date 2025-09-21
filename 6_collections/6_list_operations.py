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


def get_left_index(nums, to_find):
    index = -1
    lo = 0
    hi = len(nums)

    while lo <= hi:
        mid = (hi + lo ) // 2 # pythonic way of getting the int part of the float

        if nums[mid] < to_find:
            lo = mid + 1
        if nums[mid] > to_find:
            hi = mid - 1
        if nums[mid] == to_find:
            index = mid
            hi = mid -1
    
    return index

def get_right_index(nums, to_find):
    index = -1
    lo = 0
    hi = len(nums)

    while lo <= hi:
        mid = (hi + lo ) // 2 # pythonic way of getting the int part of the float

        if nums[mid] < to_find:
            lo = mid + 1
        if nums[mid] > to_find:
            hi = mid - 1
        if nums[mid] == to_find:
            index = mid
            lo = mid  + 1
    
    return index




def count_occurances_v3(nums, to_find):
    '''
    Returns the number of occurances in the list.
    Assumes the list is sorted.
    Gets the left most index of the item that is to be found.
    Gets the right most index of the item that is to be found.
    if left index and right index are present, then return (right index ) - (left index) + 1 is the number of occurances.
    if left or right index are -1, then no item in the list.
    '''


    left_index = get_left_index(nums, to_find)

    if left_index == -1:
        return 0
    
    right_index = get_right_index(nums, to_find)

    return right_index - left_index + 1




def builtin_count(nums, to_find):
    return nums.count(to_find)

# **** Perf test *** #

def test_custom_count(nums, to_find, repeat):
    start = perf_counter()
    num_of_occurances = 0
    for _ in range(0, repeat):
        num_of_occurances = count_occurances(nums, to_find)
    
    end = perf_counter()

    # print(f"[test custom count]     => {to_find} is found {num_of_occurances} times in the list. Time taken: {(end - start):.6f}s")
    # tuple(test case name, description, time_taken)
    return ("test_custom_count", f"{to_find} is found {num_of_occurances} times in the list", (end - start))


def test_custom_count_v2(nums, to_find, repeat):
    start = perf_counter()
    num_of_occurances = 0
    sorted_list = sorted(nums)
    for _ in range(0, repeat):
        num_of_occurances = count_occurances_v2(sorted_list, to_find)
    
    end = perf_counter()

    # print(f"[test custom count v2]  => {to_find} is found {num_of_occurances} times in the list. Time taken: {(end - start):.6f}s")
    return ("test_custom_count_v2" ,f"{to_find} is found {num_of_occurances} times in the list", (end - start))


def test_custom_count_v3(nums, to_find, repeat):
    start = perf_counter()
    num_of_occurances = 0
    sorted_list = sorted(nums)
    for _ in range(0, repeat):
        num_of_occurances = count_occurances_v3(sorted_list, to_find)
    
    end = perf_counter()

    # print(f"[test custom count v2]  => {to_find} is found {num_of_occurances} times in the list. Time taken: {(end - start):.6f}s")
    return ("test_custom_count_v3" ,f"{to_find} is found {num_of_occurances} times in the list", (end - start))

def test_builtin_count(nums, to_find, repeat):
    start = perf_counter()
    num_of_occurances = 0
    for _ in range(0, repeat):
        num_of_occurances = builtin_count(nums, to_find)
    
    end = perf_counter()

    # print(f"[test builtin count]    => {to_find} is found {num_of_occurances} times in the list. Time taken: {(end - start):.6f}s")
    return ("test_builtin_count", f"{to_find} is found {num_of_occurances} times in the list", (end - start))


def get_max_test_case_len(list_of_tuples):

    max_len = -1
    for t in list_of_tuples:
        if len(t[0]) > max_len:
            max_len = len(t[0])

    return max_len
    # 1, 4, 3


def sort_by_item_3(t):
    # assume this is a tuple with 3 or more items.
    return t[2]

def test_perf():
    lo = 1
    hi = 1000
    repeat = 100

    num_range_lo = 1
    num_range_hi = 50

    nums = []
    for _ in range(lo, hi):
        nums.append(random.randint(num_range_lo, num_range_hi))

    to_find = random.randint(num_range_lo, num_range_hi)

    results = []

    results.append(test_builtin_count(nums, to_find, repeat))
    results.append(test_custom_count(nums, to_find, repeat))
    results.append(test_custom_count_v2(nums, to_find, repeat))
    results.append(test_custom_count_v3(nums, to_find, repeat))


    max_test_case_len = get_max_test_case_len(results)

    results.sort(key=sort_by_item_3) # give the name of the function.

    result = results[0]

    print(f"*********************************************************************\n\n")
    print(f"The winner is ... {[{result[0]}]} => {result[2]:.6f}s")

    for result in results:
        print(f"[{result[0]:<{max_test_case_len}}] => {result[1]}. Time taken: {result[2]:.6f}s")


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