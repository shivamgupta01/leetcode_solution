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
#        ↑   ↑
#
# The above arrows point to positions where the corresponding bits are different.


class Solution(object):
    def hammingDistance(self, x, y):
        count = 0
        a = '{0:b}'.format(x)
        b = '{0:b}'.format(y)
        lenA = len(a)
        lenB = len(b)

        if lenA>lenB:
            while(lenA!=lenB):
                b = '0' + b
                lebB = lenB + 1
        else:
            while (lenA != lenB):
                a = '0' + a
                lenA = lenA + 1

        result = int(a) + int(b)
        result = str('{0:0100d}'.format(result))
        i =0
        while(i<len(result)):
            if int(result[i]) % 2 == 1:
                count = count + 1
            i=i+1
        return count


if __name__ == '__main__':
    s= Solution()
    print "The Hamming Distance between numbers are: " + str(s.hammingDistance(1,1727613287))
