# Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.
#
# For example, given nums = [0, 1, 0, 3, 12], after calling your function, nums should be [1, 3, 12, 0, 0].
#
# Note:
# You must do this in-place without making a copy of the array.
# Minimize the total number of operations.



class Solution(object):
    def moveZeroes(self, nums):
        i = 0
        flag = -2
        j=-2
        while(i<len(nums)-1):
            if(nums[j]==0):
                flag=j
                while(flag!=-1):
                    nums[flag] = nums[flag+1]
                    flag = flag+1
                nums[-1]=0
            j=j-1
            i=i+1




        return nums

if __name__ == '__main__':
    s = Solution()
    print "the solution is:"  + str(s.moveZeroes([0,1]))