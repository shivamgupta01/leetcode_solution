# Write a function that takes a string as input and returns the string reversed.
#
# Example:
# Given s = "hello", return "olleh".
#

class Solution(object):
    def reverseString(self, s):

        return s[::-1]


if __name__ == '__main__':
    s = Solution()
    print "The reverse string is :" + str(s.reverseString('hello'))
