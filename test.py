#!/usr/bin/env python
# -*- coding: utf-8 -*-


# The Hamming distance between two integers is the number of positions at which the corresponding bits are different.
#
# Given two integers x and y, calculate the Hamming distance.
#
# Note:
# 0 ≤ x, y < 231.
#
# Example:
#
# Input: x = 1, y = 4
#
# Output: 2
#
# Explanation:
# 1   (0 0 0 1)
# 4   (0 1 0 0)

# 1577962638
# 1727613287
#        ↑   ↑
#
# The above arrows point to positions where the corresponding bits are different.


class Solution(object):
    def hammingDistance(self, x, y):
        #
        # binary = lambda n: n > 0 and [n & 1] + binary(n >> 1) or []
        # print binary(1)
        a = '{0:b}'.format(x)
        b = '{0:b}'.format(y)
        print bin(int(a)+int(b))
        print a,b
        return None

if __name__ == '__main__':
    s= Solution()
    print "The Hamming Distance between numbers are: " + str(s.hammingDistance(1577962638,1727613287))
