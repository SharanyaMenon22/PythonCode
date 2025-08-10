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

# subscript operator.
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

# print me "Weather is hot" using the data in variables text1, text2, text3

weather = text2[0] + text2[1] + text2[2] + text2[3] + text2[4] + text2[5] + text2[6]
is_word = text1[5] + text1[6]
hot = text3[12] + text3[13] + text3[14]

print(weather + " " + is_word + " " + hot)

# in a text we can separate the words by space.
# the method used to do that is split.

text1_words = text1.split(" ")
print(text1_words)

text2_words = text2.split(" ")

print(text2_words)

text3_words = text3.split(" ")
print(text3_words)


print(text2_words[0] + " " + text1_words[1] + " " + text3_words[2])

# ['This', 'is', 'a', 'python', 'class']
# ['Weather', 'is', 'cool']
# ['Summers', 'are', 'hot']

# in a list to find out the index at which a word is there...
# we can use the method index.
# index is called on the list of words.

is_index = text1_words.index("is")
weather_index = text2_words.index("Weather")
hot_index = text3_words.index("hot")

print(text2_words[weather_index] + " " + text1_words[is_index] + " " + text3_words[hot_index])

print(text2.index("Weather"))

text = "This is a python class"

print("Index of the word python: ", text.index("python"))

'''
How to search for a text that is not of the same case?
  1. Ask python to ignore the case that we are looking for ⛔
  2. How about make the case same for the source and the text to find as same? 
'''

text_upper = text.upper()
python_upper = "Python".upper()

print("Index of the word Python: ", text_upper.index(python_upper))


print("Prints true or false:", text.endswith("class"))





