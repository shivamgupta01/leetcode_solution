'''
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers x and y, calculate the Hamming distance.

Note:
0 ≤ x, y < 231.

Example:

Input: x = 1, y = 4

Output: 2

Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑

The above arrows point to positions where the corresponding bits are different.
'''
class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        x1 = self.helper(x)
        y1 = self.helper(y)
        count = 0
        if len(x1) > len(y1):
            count = self.helper_new(x1,y1)
        
        elif len(x1) < len(y1):
            count = self.helper_new(y1,x1)
        else:
            i = 0
            while i<len(x1):
                if x1[i] + y1[i] == 1:
                    count = count + 1
                i = i + 1
        return count

    def helper_new(self,x1,y1):
        i = 0
        count = 0
        while i < len(y1):
            if x1[i] + y1[i] == 1:
                count = count + 1
            i = i + 1
        while i < len(x1):
            if x1[i] == 1:
                count = count + 1
            i = i + 1
        return count

    def helper(self,x):
        temp = []
        while x:
            if x % 2 == 0:
                temp.append(0)
            else:
                temp.append(1)
            x = x // 2 
        return temp

s = Solution()
print(s.hammingDistance(1,3))