"""

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

"""


def twoSums(nums, target):
    """
    :param nums:
    :param target:
    :return: List with indices.
    """
    temp_dict = {}
    i = 0
    if len(nums) == 2:
        return [0,1]
    while i < len(nums):
        temp_dict[nums[i]] = i
        i += 1
    i = 0
    while True:
        x = target - nums[i]
        if x in temp_dict and i != temp_dict[x]:
            return [i, temp_dict[x]]
        i += 1


            


result = twoSums(nums=[3, 2, 3], target=6)

print(result)
