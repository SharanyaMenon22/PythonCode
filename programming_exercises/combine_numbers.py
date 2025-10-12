

import string

def combine_numbers(ulimit):
    stream_of_str = map(str, range(1, ulimit + 1))
    return ",".join(stream_of_str)

def append_comma(number):
    return str(number) + ","

def join_numbers_to_a_string_v1(ulimit):
    result = ""
    for i in range(1, ulimit + 1):
        result += append_comma(i)
    return result[:-1]

def join_numbers_to_a_string_v2(ulimit):
    return combine_numbers(ulimit)


# print(join_numbers_to_a_string_v1(1_000000))  # "1,2,3,4,5"

print(join_numbers_to_a_string_v2(5_000000))  # "1,2,3,4,5"
