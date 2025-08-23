'''
We want to avoid repeating of the implementation / behavior of the program
We also like to keep things concise.

syntax:
  def <method>():
    ,,,,
    ....
    return <value>
'''

# Num1:{} gets added to Num2:{} and the result is {}

def print_message(num1, op, num2, result):
    print(f"Num1: {num1} {op} Num2:{num2} and the result is {result}")    

def add(num1, num2):
    '''
      This adds 2 numbers.
    '''
    result = num1 + num2
    print_message(num1, 'gets added to', num2, result)

def subtract(num1, num2):
    result = num1 - num2
    print_message(num1, 'gets subtract by', num2, result)

def multiply(num1, num2):
    result = num1 * num2
    print_message(num1, 'is multiplied by', num2, result)


def divide(num1, num2):
    '''
    Divides num1 with num2. num2 is expected to be non-zero. Otherwise, prints error message.
    '''
    if num2 != 0:
        result = num1 / num2
        print_message(num1, 'is divided by', num2, result)
    else:
        print(f"Can't divide by zero")    

num1 = float(input("Enter a number:"))
num2 = float(input("Enter the next number:"))
op = input("Enter arithmetic op(+, -, *, /):")



op = op.strip()

if op == '+':
    add(num1, num2)
elif op == '-':
    subtract(num1, num2)
elif op == '*':
    multiply(num1, num2)
elif op == '/':
    divide(num1, num2)    
else:
    print("Invalid operation.Please specify (+, -, *, /)")