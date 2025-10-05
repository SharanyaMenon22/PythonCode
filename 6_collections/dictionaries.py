
"""
Like physical dictionaries, in python we store the items in the dictionary by key -> value.

my_dict = dict()
my_dict = {}

my_dict = { 1 : "one", 2 : "two" }
my_dict[1] ==> "one"
"""

my_dict = { 3 : "three", 1: "one", 2 : "two"}

print(my_dict)

print(my_dict[1])
# print(my_dict[4]) -- results in key error as key is not present in the dict.

if 4 in my_dict:
    print("4 is in the dictionary")
else:
    print("4 is not in the dictionary")
    my_dict[4] = "four"

print("After adding 4 to the dictionary ")
print(my_dict)

"""
keys can have...
int
float
string
tuple

keys cannot have list

my_dict = { [1,2,3,4] : "list till 4"} ⛔

my_dict = { (1,2,3,4) : "tuple till 4" } ✅

"""

capitals = {
    "India" : "New Delhi",
    "US" : "Washington DC",
    "UK" : "London",
    "France" : "Paris"
}

for key, value in capitals.items():
    print(f"{key} => {value}")

print(capitals["India"])


print("\nOnly keys...\n")

for key in capitals.keys():
    print(key)

print("\n\nOnly values...\n")

for value in capitals.values():
    print(value)



"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3, 5], target = 11
Output: [0,1]

Input: nums = [3,2,4], target = 6
Output: [1,2]

# value : index
{ 3 : [0, 1], 2 : 1, 4: 2 }

"""
print("Two sum...")

value_index_dict = dict()
target = 7
nums = [1, 2, 3, 4, 1]

# {1 : 0}
# { 1 : 0, 2: 1}
# { 1 : 0, 2 : 1, 3 : 2}
# { 1 : 0, 2 : 1, 3 : 2 } => [2, 3]

# resultant_indices = []
# found = False
# for index, num in enumerate(nums):
#     if found:
#         break

#     # if num == target:
#     #     resultant_indices.append(index)
#     # else:
#     #     list_of_indices = value_index_dict.get(num, [])
#     #     list_of_indices.append(index)
#     #     if sum(list_of_indices) == target:
#     #         break
#     sum = 0

#     for key, value in value_index_dict.items():
#         temp = 0
#         for _ in value:
#             temp += key
#         if temp + num == target:
#             resultant_indices.append(index)
#             resultant_indices.extend(value)
#             found = True
#             break
#         if found:
#             break
            
#     list_of_indices = value_index_dict.get(num, [])
#     list_of_indices.append(index)         
#     value_index_dict[num] = list_of_indices       
# print(sorted(resultant_indices))




value_index_dict = {}
list_of_indices = []
for index, num in enumerate(nums):
    compliment = target - num
    if compliment in value_index_dict:
        list_of_indices.append(index)
        list_of_indices.append(value_index_dict[compliment])
        break
    else:
        value_index_dict[num] = index

print(sorted(list_of_indices))