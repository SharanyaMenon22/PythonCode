'''
Get a user input to get a number.
Get a user input to get +,- , * , /
Based on the input, we do the arithmetic operation and print the result.
'''


num1 = float(input("Enter a number:"))
num2 = float(input("Enter the next number:"))
op = input("Enter arithmetic op(+, -, *, /):")

op = op.strip()

if op == '+':
    result = num1 + num2
    print(f"{num1} {op} {num2} = {result}")
elif op == '-':
    result = num1 - num2
    print(f"{num1} {op} {num2} = {result}")
elif op == '*':
    result = num1 * num2
    print(f"{num1} {op} {num2} = {result}")
elif op == '/':
    result = num1 / num2
    print(f"{num1} {op} {num2} = {result}")
else:
    print("Invalid operation.Please specify (+, -, *, /)")

'''
Observations when running the code:
- The program assumes the input to be int() and if we get float() it crashes. ⛔
- Float point divisions work. ✅
- For the operations, we can try strip off the space and see if they are one of the given operations. ✅

Observations for the implementation ( code ):
- A bit code duplication happening w.r.t. printing of the result.
'''