'''
Trying to implement more functions.
'''


# program to check if the number is even or odd.

def is_even(number):
    # if number % 2 == 0:
    #     print(f"{number} is even")
    # else:
    #     print(f"{number} is odd")

    if number % 2 == 0:
        return True
    else:
        return False


number = int(input("Enter a number: " ))
response = is_even(number)
print(f"{number} is {response}")


