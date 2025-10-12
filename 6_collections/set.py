# set has unique items... unlike dictionary, it does not have a value.

nums = [1, 2, 3, 4, 1]

nums_set = set()

for num in nums:
    nums_set.add(num)

print(nums_set)


words = ["is", "a", "good", "language", "is"]

words_set = set(words)

print(words_set)