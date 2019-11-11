"""
Given an array of integers, find if the array contains any duplicates.

Your function should return true if any value appears at least twice in the array,
and it should return false if every element is distinct.

Example 1:

Input: [1,2,3,1]
Output: true
Example 2:

Input: [1,2,3,4]
Output: false
Example 3:

Input: [1,1,1,3,3,4,3,2,4,2]
Output: true
"""


def containsDuplicate(nums):
    """
     Evaluate if list contains duplicates.
    :param nums: List(int)
    :return: Boolean
    """
    dict_nums = {}
    for val in nums:
        if val in dict_nums.keys():
            return True
        dict_nums[val] = 0
    return False


print(containsDuplicate([1, 3, 3, 4]))
