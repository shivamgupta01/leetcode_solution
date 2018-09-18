#   Reverse Integer
# Given a 32-bit signed integer, reverse digits of an integer.
#
# Example 1:
#
# Input: 123
# Output:  321
# Example 2:
#
# Input: -123
# Output: -321
# Example 3:
#
# Input: 120
# Output: 21
# Note:
# Assume we are dealing with an environment which could only hold integers within the 32-bit signed integer range. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.



class Solution(object):
    def reverse(self, x):
        isNegative = False
        reversed_num = 0
        if x == 0:
            return 0
        elif x < 0:
            isNegative = True
            x = x * -1
        while x>0:
            reversed_num = reversed_num * 10 + x%10
            x = int(x/10)
        
        if isNegative == False:
            if reversed_num <= 2147483647:
                return reversed_num
            else:
                return 0
        else:
            if reversed_num <= 2147483648:
                return -1 * reversed_num
            else:
                return 0







if __name__ == '__main__':
    s=Solution()
    print("Solution is : " + str(s.reverse(-123))) 