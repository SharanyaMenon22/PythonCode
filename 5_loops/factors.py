

'''
Print the factors of a number

Enters a number : 16
Prints factors of 16
1
2 
4
8
16


1 no need to check
..
...
8 ...
9 ?
10 ?
11 ?
12 ?
13 ?
14 ? 
15 ?
16 //

1
2
3
4
5
6
7
8
9
10


16 no need to check
'''


def print_factors(num):   
    # factor is something that perfectly divides a number. Reminder is 0. % is to see to get reminders.
    print(f"1 is a factor of {num}")
    for i in range(2, int((num / 2) + 1)):
        if num % i == 0:
            print(f"{i} is a factor of {num}")
    print(f"{num} is a factor of {num}")

num = int(input("Enter a number: ").strip())
print_factors(num)