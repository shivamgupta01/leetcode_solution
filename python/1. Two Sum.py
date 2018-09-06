"""

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

"""


def twoSums(nums, target):
    for i in range(len(nums)):
        for j in (range(len(nums))):
            # print j
            if (nums[i] + nums[j] == target):
                if i != j:
                    return i, j
            


result = twoSums(nums=[3, 2, 4], target=6)

print(result)
