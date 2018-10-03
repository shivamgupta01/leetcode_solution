'''
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

[-4,-1,-1,0,1,2]

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
'''
from itertools import permutations
class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # Without repetition.
        # nums_index = [True] * len(nums)
        # nums = sorted(nums)
        # temp = []
        # mid_negative = False
        # if nums[len(nums)//2] <0:
        #     mid_negative == True
        # res = []
        
        # i = len(nums)//2
        # while i >-1 and i < len(nums):
        #     if nums_index[i] == True:
        #         temp.append(nums[i])
        #         nums_index[i] = False
        #     if sum(temp) == 0 and len(temp) == 3:
        #         res.append(temp)
        #         temp = []
                
        #         continue
        #     if sum(temp) < 0:
        #         i = i + 1
        #     else:
        #         i = i - 1
        # return res
        # nums = sorted(nums)
        if len(nums)<3:
            return []
        mi = min(nums)
        mx = max(nums)
        i = 0
        j = 0
        res = set()

        while i < len(nums):
            j = 0
            while j < len(nums):
                if i != j:
                    if (-1 * (nums[i] + nums[j]) >= mi and\
                            -1 * (nums[i] + nums[j]) <= mx):
                            if -1 * (nums[i] + nums[j]) in nums[0:min(i,j)] + nums[min(i,j)+1:max(i,j)] + nums[max(i,j)+1:len(nums)]:
                                
                                temp =sorted([nums[i],nums[j],-1 * (nums[i]+nums[j])])
                                temp = tuple(temp)
                                res.add(temp)
                j = j + 1
            i = i + 1
        return [list(i) for i in res]
        

        
s = Solution()
print(s.threeSum([-1, 0, 1, 2, -1, -4]))