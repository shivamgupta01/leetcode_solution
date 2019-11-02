# Given a sorted array, remove the duplicates in-place such that each element appear only once and return the new length.
#
# Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
#
# Example:
#
# Given nums = [1,1,2],
#
# Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.
# It doesn't matter what you leave beyond the new length.


class Solution(object):
    def removeDuplicates(self, nums):
        if len(nums) == 0:
            return 0
        i, j = 0, 1
        while i < len(nums) - 1:
            if nums[i] != nums[i+1]:
                nums[j] = nums[i+1]
                j = j + 1
            i = i + 1
        return j



if __name__ == '__main__':
    s = Solution()
    print("the soution is : " + str(s.removeDuplicates([1])))