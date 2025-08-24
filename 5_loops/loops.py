'''

loop <until a condition is met / true >:
   do work


while loop:

while <condition is met>:
   do work




for loop

in other languages.
i = 0
condtion = 5
<initial state>; check if the condition is valid; <change the state>
   do work

   
python:
   for loop through by <getting a range of items>
'''

# Looping through 1000 times.
i = 1
while i <= 1000:
    print("Hello, world!")
    i += 1


while False:
    print("Hello, Python enthusiasts...")


# for loop.
                         #👇 step
for num in range(1, 10001, 1):
    print(num)




# Let's we want to create a function that doubles a number by given number of times.
# i.e. user enters a number and the number of times they want to double it.
# The function returns the final result.
# user enters
# number: 2
# number of times to double: 3

# 2 * 2 = 4
# 4 * 2 = 8
# 8 * 2 = 16
# return 16 as a result.


def doubles( num, num_times):
    ''' 
      loop through num_times and double the number. Store the result. Return the final result.
    '''

    i = 1
    while i <= num_times:
        num = num * 2
        print(f"After doubling {i} times : {num}")
        i += 1
    return num


num = int(input("Enter num to be doubled: "))
num_times = int(input("Number of times to be double: "))
result = doubles( num, num_times )
print(f"{num} doubled {num_times} times and the result is {result}")



'''
Let's say a person invested 1000$ for 5 years.
A interest of 2% is accured for each year.
What is the final amount after 5 years.
'''
def investment( principle, No_years):
    Interest = 2/100
    i = 1
    while i <= No_years:
        principle = principle + principle * Interest
        print(f"After {i} years: {principle:.2f}")
        i+=1 
    return principle

principle = 100
No_years = 5
result = investment(principle, No_years)
print(result)



