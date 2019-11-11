"""
Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Note:

Each element in the result should appear as many times as it shows in both arrays.
The result can be in any order.
Follow up:

What if the given array is already sorted? How would you optimize your algorithm?
What if nums1's size is small compared to nums2's size? Which algorithm is better?
What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?
"""
import collections


def intersect(nums1, nums2):
    """
    Given two arrays, this function compute their intersection.
    :param nums1: List(int)
    :param nums2: List(int)
    :return: List(int)
    """
    counter_nums1 = collections.Counter(nums1)
    counter_nums2 = collections.Counter(nums2)
    intersection_list = list((collections.Counter(nums2) & \
                              collections.Counter(nums1)).keys())
    res = []
    for i in intersection_list:
        for val in range(0,min(counter_nums1[i], counter_nums2[i])):
            res.append(i)
    return res


print(intersect([4, 9, 5], [9, 4, 9, 8, 4]))
