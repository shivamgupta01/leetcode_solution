'''
Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

The update(i, val) function modifies nums by updating the element at index i to val.

Example:

Given nums = [1, 3, 5]

sumRange(0, 2) -> 9
update(1, 2)
sumRange(0, 2) -> 8
Note:

The array is only modifiable by the update function.
You may assume the number of calls to update and sumRange function is distributed evenly.
'''
class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        
        self.nums = nums
        if len(self.nums) == 0:
            return None
        i = 0
        self.update_lst = {}
        self.nums_sum = [nums[0]]
        while i<len(nums)-1:
            self.nums_sum.append(nums[i+1] + self.nums_sum[i])
            i = i + 1
        
        
    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: void
        """
        self.update_lst[i] = val
        


    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        range_sum = 0
        if i == 0:
            range_sum =  self.nums_sum[j]
        else:
            range_sum = self.nums_sum[j] - self.nums_sum[i-1]
        for item,val in self.update_lst.items():
            if item > i-1 and item < j+1:
                range_sum = range_sum + val - self.nums[item]
        return range_sum
        
                    


# Your NumArray object will be instantiated and called as such:
obj = NumArray([5,18,13])
# [5,23,36]

print(obj.sumRange(0,2))
# print(obj.sumRange(0,1))
obj.update(1,-1)
obj.update(2,3)
obj.update(0,5)
obj.update(0,-4)
print(obj.sumRange(0,2))
