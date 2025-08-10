'''
To accept input from the user, the method used in input()
This method prompts the user to enter the value / text
and then returns a string.
'''


text = input("Enter a text: ")
print("We got the input as ", text)

# We are getting strings here.. 
num = input("Enter a number: ")
print("We got the number:", num)
print("Multiply the number by 2: ", num * 2)

# The text can be casted to number using int(), float()
# int - 0, 1, 2 , ....
# float - 1.0, 2.0, 3.0, ....

# we will cast the string to number.

# num = input("Enter a number: ")
num = int(num)
print("Multiply the number by 2: ", num * 2)

# can even be casted in one line.
num = int(input("Enter a num:"))
print("Multiply the number by 2: ", num * 2)


# Get an input from the user and print the first character.

text = input("Enter text:")
print("The first character:", text[0])

# To remove the leading and trailing spaces , we use strip

# text = input("Enter text: ")

print("*", text, "*")
print("*", text.strip(), "*")


text = "The cost of the PC is"
cost = 2000

print(text, cost)

# print using f-strings
print(f"{text} {cost * 2}")