
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
nums = [1, 3, 2, 5, 1]







# {1 : 0}
# { 1 : 0, 3: 1}
# { 1 : 0, 3 : 1, 2 : 2}
# { 1 : 0, 2 : 1, 3 : 2 } => [2, 3]


# value_index_dict = {}
# list_of_indices = []
# for index, num in enumerate(nums):
#     compliment = target - num
#     if compliment in value_index_dict:
#         list_of_indices.append(index)
#         list_of_indices.append(value_index_dict[compliment])
#         break
#     else:
#         value_index_dict[num] = index

# print(sorted(list_of_indices))


# Minimal, safe single-pass two-sum implementation and invocation
def two_sum(nums, target):
    """Return indices of two numbers that add up to target, or None."""
    seen = {}
    for i, n in enumerate(nums):
        comp = target - n
        if comp in seen:
            return [seen[comp], i]
        seen[n] = i
    return None


result = two_sum(nums, target)
if result:
    print(f"Two-sum result: indices={result}, values={[nums[i] for i in result]}")
else:
    print("Two-sum: no solution")



# Get me the count of each repeated numbers in the list.
nums = [1,2,1,3,4,1,5, 5] # { 1 : 3, 2 : 1, 3 : 1, 5 : 2 }

occurences = {}

for num in nums:
    count = occurences.get(num, 0)
    occurences[num] = count + 1

print(occurences)

nums = [1,2,3,4,5,6]
# group the numbers by even and odd. {'even': [2,4,6], 'odd': [1,3,5]}

even_odd_dict = {}
for num in nums:
    even_or_odd = 'even' if num % 2 == 0 else 'odd'
    list_of_nums = even_odd_dict.get(even_or_odd, [])
    list_of_nums.append(num)
    even_odd_dict[even_or_odd] = list_of_nums


print(even_odd_dict)

