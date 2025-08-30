'''
We have a long string with line breaks. But the column length of the string is more than 120.
The code should read the text and break the string so that the column length is <= 120.
But the breaking of lines should be such that the words should not broken down into 2 separate lines. ⛔

'''

# long text
text = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis 
nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
"""


'''

1. break the text into multiple lines so that we get a list of lines.... ✅
2. Now, go through each line ✅
3. for the line, keep taking the text / characters until we reach 120 characters or till a word that is <= 120 characters.✅
4. for the rest of the line, again check if it is >= 120 and repeat step 3 or else just print that line.
5. go to step 2.
'''

lines = text.split("\n")
for line in lines:
    len_of_line = len(line)    
    curr_idx = 0
    while ( len_of_line >= 120 ):
        part_of_line = line[curr_idx:curr_idx + 119]

        # Need to check if we have space next or not. if not go backwards to find space and take the text only till then.
        if line[curr_idx:curr_idx + 120] != ' ':
            index = part_of_line.rfind(' ')
            part_of_line = line[curr_idx: curr_idx + index]
            curr_idx = curr_idx + index
        else:
            curr_idx = curr_idx + 119


        print(part_of_line)        
        len_of_line = len_of_line - len(part_of_line)
    print(line[curr_idx:])
