# Text is represented by a data type called string 
# string is a type where we can store, alphabets, numbers, space, or any character. 


text = "This is python class. This is going well. We kind of like it. Hope so"

print(text)

# The string / text in python is in a form of container.
# Where each character can be accessed via the index of the container.
# The index starts at 0.
# The first character is accessed by using text[0]

print("Printing the first character", text[0])
print("Printing the second character", text[1])

print("Printing some random character", text[19])

# we get the length of the string using len() method

length_of_text = len(text)

print("The length of the text", length_of_text)

print("Printing the last character of the text", text[length_of_text -1 ])

# printing with larger index than the length of the text

# print("Printing with larger index than the length of the text", text[1000])

# multi-line string
text = "abc def \
ghi jkl "

print(text)

# yet another multi-line string

text = """
abc def
ghi jkl
"""

print(text)

first_name = "Sharanya"
last_name = "Menon"

# print it in a format of <first_name>, <last_name>

print(first_name, ",", last_name)

# strings can be joined with +

full_name = first_name + last_name

print("Full Name:", full_name)

# Getting it right.
full_name = first_name + ", " + last_name

print("Full Name:", full_name)

text1 = "This is a python class"
text2 = "Weather is cool"
text3 = "Summers are hot"

# print me "Weather is hot"





