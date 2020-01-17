# Write a function that takes a string as input and returns the string reversed.
#
# Example:
# Given s = "hello", return "olleh".
#

class Solution(object):
    def reverseString(self, s):
        i, j = 0, len(s)-1
        while i < j:
            s[i], s[j] = s[j], s[i]
            i,j = i+1, j-1
        return s


if __name__ == '__main__':
    s = Solution()
    print("The reversed string is :" + str(s.reverseString(['h','e','l','l','o'])))
