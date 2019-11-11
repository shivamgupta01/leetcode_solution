# Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.
#
# For example, given nums = [0, 1, 0, 3, 12], after calling your function, nums should be [1, 3, 12, 0, 0].
#
# Note:
# You must do this in-place without making a copy of the array.
# Minimize the total number of operations.


class Solution(object):
    def moveZeroes(self, nums):
        """
        :param nums:
        :param List:
        :return: List
        """
        zeros = 0
        current_pointer = 0
        while current_pointer < len(nums):
            if nums[current_pointer] == 0:
                zeros += 1
            else:
                nums[current_pointer - zeros] = nums[current_pointer]
            current_pointer += 1
        current_pointer = len(nums) - zeros
        while current_pointer < len(nums):
            nums[current_pointer] = 0
            current_pointer += 1
        return nums


if __name__ == '__main__':
    s = Solution()
    print(s.moveZeroes([0, 1, 0, 3, 12]))
