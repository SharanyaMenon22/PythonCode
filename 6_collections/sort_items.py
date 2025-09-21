

def sort_by_2_value(t):
    # assuming that this tuple has more than 1 items/values
    return t[1]


def main():
    nums = [1,2,3,5,4]

    print(nums)

    sorted_nums = sorted(nums) # if we don't want to change the original list.

    print(sorted_nums)

    print(f"Original nums:{nums}")


    nums.sort(key=None, reverse=True) # if we are fine with changing the original list.

    print(f"Original nums: {nums}")

    # tuple... 
    nums_tuple = [("one", 1), ("two", 2), ("four", 4), ("three", 3)]

    nums_tuple.sort()

    print(f"After sorting: {nums_tuple}")

    nums_tuple.sort(key=sort_by_2_value)

    print(f"After sorting using a key : {nums_tuple}")

    


if __name__ == '__main__':
    main()