'''
Given an integer, write a function to determine if it is a power of three.

Example 1:

Input: 27
Output: true
Example 2:

Input: 0
Output: false
Example 3:

Input: 9
Output: true
Example 4:

Input: 45
Output: false
Follow up:
Could you do it without using any loop / recursion?
'''
import math
class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <1:
            return False
        if n == 1:
            return True
        return self.helper(n)
        
    def helper(self,n):
        if n % 3 == 0:
            if int(n/3) == 1:
                return True
            return self.helper(n/3)
        else:
            return False
s = Solution()
print(s.isPowerOfThree(243))
