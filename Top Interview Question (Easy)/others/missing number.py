#   Missing Number
# Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.
#
# Example 1
#
# Input: [3,0,1]
# Output: 2
# Example 2
#
# Input: [9,6,4,2,3,5,7,0,1]
# Output: 8
#
# Note:
# Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?
#
# Credits:
# Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.

class Solution(object):
    def missingNumber(self, nums):
        # d={}
        # max_number = max(nums)
        # min_number = min(nums)
        # if max_number-min_number==len(nums)-1 and min_number==0:
        #     return max_number+1
        # elif max_number-min_number==len(nums)-1:
        #     return min_number-1
        # else:
        #     while min_number <= max_number:
        #         d[min_number] = 1
        #         min_number += 1
        #     for key in nums:
        #         if key in d:
        #             d[key]-=1
        #     for key,value in d.iteritems():
        #         if value == 1:
        #             return key


        min_number = min(nums)
        d={}
        sum_n=(((min_number+len(nums))*(min_number+len(nums)-1))/2)











if __name__ == '__main__':
    s = Solution()
    print "solution is : " +str(s.missingNumber([3,4,6]))