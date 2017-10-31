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
        i = 0
        a = '{0:b}'.format(x)
        b = '{0:b}'.format(y)
        print a
        print b
        lenA = len(a)
        lenB = len(b)
        if lenA>lenB:
            counter = lenA - lenB
            while(lenA>=lenB and lenB != 0):
                if a[lenA-1]!=b[lenB-1]:
                    count = count +1

                lenA = lenA -1
                lenB = lenB -1

            while (lenA>0):
                if int(a[lenA-1]) ==0:
                    counter = counter -1
                lenA = lenA -1
            count = int(count) + int(counter)

        elif lenB>lenA:
            counter = lenB - lenA
            while(lenB>=lenA and lenA != 0):
                if a[lenA-1]!=b[lenB-1]:
                    count = count +1
                lenB = lenB - 1
                lenA = lenA - 1

            while (lenB>0):
                if int(b[lenB-1]) ==0:
                    counter = counter -1
                lenB = lenB -1
            count = int(count) + int(counter)

        else:
            result = int(a) + int(b)
            result = str('{0:d}'.format(result))
            while(i<len(result)):
                if int(result[i]) % 2 == 1:
                    count = count + 1
                i=i+1

        return count


if __name__ == '__main__':
    s= Solution()
    print "The Hamming Distance between numbers are: " + str(s.hammingDistance(1,4))
