'''
We have a long string with line breaks. But the column length of the string is more than 120.
The code should read the text and break the string so that the column length is <= 120.
But the breaking of lines should be such that the words should not broken down into 2 separate lines. ⛔

'''

# long text

'''

1. break the text into multiple lines so that we get a list of lines.... ✅
2. Now, go through each line ✅
3. for the line, keep taking the text / characters until we reach 120 characters or till a word that is <= 120 characters.✅
4. for the rest of the line, again check if it is >= 120 and repeat step 3 or else just print that line.
5. go to step 2.
'''

'''
column count: 5

abc defghi jklm
nopqr stuvw xyz
'''

'''
abc
defghi
jklm
nopqr
stuvw
xyz
'''

def get_word(tmp, line):
    tmp = str(tmp)
    line = str(line)

    # the length of original string and substring is the same
    if len(line) == len(tmp):
        return tmp
    
    # let's backtrack to find a space.
    # abc def ghijklmn
    index = line.rfind(' ', 0, len(tmp))
    if index != -1: # we found a space while backtracking.
        return line[0: index]
    
    # we could not find space while backtracking...
    # so let's do a forward search
    index = line.find(' ', len(tmp) -1)
    if index != -1: # there is space.
        return line[0: index]
    
    return line



def line_wrap( text, column_count):
    # split the text by line breaks.
    lines = str(text).split('\n')

    for line in lines:
        
        while line:
            if len(line) >= column_count: # difficult part.
                # get the substring from first index to the column_count.
                line = line.lstrip(' ')
                tmp = line[0: column_count]
                tmp = get_word(tmp, line)
                # update the line so that we remove the tmp from the line.
                line = line[len(tmp): ]
                print(tmp)

            else:
                print(line)
                break





text = '''
abc defghi jklm
nopqr stuvw xyz
12345
'''

line_wrap(text, 5)

text = '''
abc
def
ghi
123455566 7890
'''

line_wrap(text, 5)