

'''
tuples are sequenced collections.
tuples are immutable.
tuples can be returned from a function, thereby allowing python to return multiple values.
tuples can be looped through.
They are created using ( 1, 2, 3 )
'''

numbers = (1,2,3)

print(numbers)

for num in numbers:
    print(num)


# you can divide the tuples and assign them to individual values.

one, rest, _ = numbers
print("Dividing the tuple into different values ")
print(one)
print(rest)

my_tuple = (one, rest)

print(f"Printing {my_tuple}")



def to_check_in_tuple(my_tuple, number):
    print(f"Checking if {number} is in {my_tuple}")

    if number in my_tuple:
        print("Yes")
    else:
        print("No")



to_check_in_tuple(numbers, 1)
to_check_in_tuple(numbers, 4)



# Let's say you have a list of numbers and get me the only ones that are even.

def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False
    
def is_odd(number):
    # if is_even(number) == False:
    #     return True
    # else:
    #     return False

    return is_even(number) == False

def get_evens(numbers):
    '''
        this method loops through the list of numbers
        and collects the evens 
        and returns them ....
    '''
    print("Printing evens...")
    for num in numbers:
        if is_even(num) == True:
            print(num)

def get_odds(numbers):
    print("Printing odds...")
    for num in numbers:
        if is_odd(num) == True:
            print(num)


#### [1,2,3,4,5,6] => [2, 4, 6]


get_evens((1,2,3,4,5,6))

get_odds((1,2,3,4,5,6))