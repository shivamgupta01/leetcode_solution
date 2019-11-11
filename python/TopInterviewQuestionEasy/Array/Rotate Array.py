"""
Given an array, rotate the array to the right by k steps, where k is non-negative.

Example 1:

Input: [1,2,3,4,5,6,7] and k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
Example 2:

Input: [-1,-100,3,99] and k = 2
Output: [3,99,-1,-100]
Explanation:
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
Note:

Try to come up as many solutions as you can,
there are at least 3 different ways to solve this problem.
Could you do it in-place with O(1) extra space?
"""


def rotate(nums, k) -> None:
    """
    Rotate Array k times in Place.
    :param nums: list
    :param k: int
    :return: None
    """
    i = 0
    k = k % len(nums)
    count = 0

    while count < len(nums):
        temp = i
        cur = nums[temp]
        while True:
            temp = (temp + k) % len(nums)
            next_value = nums[temp]
            nums[temp] = cur
            cur = next_value
            count = count + 1
            if i == temp:
                break
        i = i + 1
    print(nums)


print(rotate([1, 2, 3, 4, 5, 6, 7], 3))
