
'''
lists a list of items... which can be numbers, strings, decimals, boolean, or even any complex types.
They are not ordered.
They are mutable ( can be modified.)
they can be sorted.
we can find items in them...

can be defined using []
'''


numbers = [1, 2, 3, 4, 5]

print(numbers)

print("Loop through")
for num in numbers:
    print(num)


numbers.append(6)
print("After appending 6.")
print(numbers)



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
    evens = [] # empty list.
    for num in numbers:
        if is_even(num) == True:
            evens.append(num) # keep appending the evens.
    
    return evens

def get_odds(numbers):
    print("Printing odds...")
    odds = [] # empty list
    for num in numbers:
        if is_odd(num) == True:
            odds.append(num)
    
    return odds




evens = get_evens([1,2,3,4,5])

print(evens)


odds = get_odds([1,2,3,4,5])

print(odds)


print(f"f is at {odds.index(5)}")


# square up all the numbers in the list.

def squares(numbers):
    squares = []
    for num in numbers:
        squares.append(num * num)

    return squares



numbers = [1,2,3,4,5]
print(f"{numbers} are squared:" )
sq = squares(numbers)
print(sq)


numbers.reverse()
print("Reversing the list.")
print(numbers)

numbers.append(7)
numbers.append(6)
numbers.append(8)


print(f"numbers is now... {numbers}")

print("sort the numbers...")

numbers.sort()
print(f"After sorting... {numbers}")

numbers.append(5)
print(f"The list is {numbers}")

numbers.remove(5)

print(f"After removing 1st occurance of 5, the list is {numbers}")