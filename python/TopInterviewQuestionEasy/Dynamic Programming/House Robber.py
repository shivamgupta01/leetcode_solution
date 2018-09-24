#   House Robber
# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.
#
# Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.
#
# Credits:
# Special thanks to @ifanchu for adding this problem and creating all test cases. Also thanks to @ts for adding additional test cases.


class Solution(object):
    def rob(self, nums):
        temp1 = 0
        temp2 = 0
        for i in range(len(nums)):
            if i%2 == 0:
                temp1 = max(temp1 + nums[i],temp2)
            else:
                temp2 = max(temp2 + nums[i],temp1)

        return max(temp1,temp2)
if __name__ == '__main__':
    s = Solution()
    print("Solution is :" + str(s.rob([3,2,3,4,3,2,1,3,4,5,6,5,4,3])))

