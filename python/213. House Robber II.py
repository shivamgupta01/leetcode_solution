'''
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

Example 1:

Input: [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2),
             because they are adjacent houses.
Example 2:

Input: [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.
'''

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        elif len(nums) <= 3:
            return max(nums)

        sum1,sum2 = 0,0
        temp1,temp2 = 0,0
        num1 = nums[0:-1]
        for i in range(len(num1)):
            if i % 2 == 0:
                temp1 = max(temp1 + num1[i],temp2)
            else:
                temp2 = max(temp2 + num1[i],temp1)
        sum1 =  max(temp1,temp2)
        num2 = nums[1:]
        temp1,temp2 = 0,0
        for i in range(len(num2)):
            if i % 2 == 0:
                temp1 = max(temp1 + num2[i],temp2)
            else:
                temp2 = max(temp2 + num2[i],temp1)
        sum2 = max(temp1,temp2)
        return max(sum1,sum2)

        
if __name__ == '__main__':
    s = Solution()
    print(s.rob([1,7,9,2]))