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
        if x>=0:
            if not(int(int("".join(list(str(x))[::-1])))>>32):
                return int("".join(list(str((x)))[::-1]))
            else:
                return x
        else:
            if not(int(int("".join(list(str(abs(x)))[::-1]))*-1)>>32):
                print int("".join(list(str(abs(x)))[::-1]))
                return int("".join(list(str(abs(x)))[::-1]))*-1
            else:
                return x






if __name__ == '__main__':
    s=Solution()
    print "Solution is : " + str(s.reverse(-321))