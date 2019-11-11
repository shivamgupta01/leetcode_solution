"""
Given a non-empty array of integers,
every element appears twice except for one.
Find that single one.

Note:

Your algorithm should have a linear runtime complexity.
Could you implement it without using extra memory?

Example 1:

Input: [2,2,1]
Output: 1
Example 2:

Input: [4,1,2,1,2]
Output: 4
"""


def singleNumber(nums):
    """
    Return the int which occurs only once.
    :param nums: list(int)
    :return: int
    """
    temp_dict = {}
    for val in nums:
        if val in temp_dict.keys():
            del temp_dict[val]
        else:
            temp_dict[val] = True
    return next(iter(temp_dict))


singleNumber([1, 1, 2, 3, 3])
