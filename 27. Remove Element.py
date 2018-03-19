# Given an array and a value, remove all instances of that value in-place and return the new length.
#
# Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
#
# The order of elements can be changed. It doesn't matter what you leave beyond the new length.
#
# Example:
#
# Given nums = [3,2,2,3], val = 3,
#
# Your function should return length = 2, with the first two elements of nums being 2.

class Solution(object):
    def removeElement(self, nums, val):
        i = 0
        flag = -2
        j = -2
        count = 0
        while (i < len(nums) - 1):
            if (nums[j] == val):
                flag = j
                while (flag != -1):
                    nums[flag] = nums[flag + 1]
                    flag = flag + 1
                nums[-1] = val
            j = j - 1
            i = i + 1
        for i in nums:
            if i !=val:
                count=count+1
        return count

if __name__ == '__main__':
    s = Solution()
    print "solution is: " + str(s.removeElement([3,2,2,1,2,3,4],3))