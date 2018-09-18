# Write a function that takes a string as input and returns the string reversed.
#
# Example:
# Given s = "hello", return "olleh".
#

class Solution(object):
    def reverseString(self, s):
                right = len(s)-1
                s1=[]
                while(right>=0):
                    s1.append(s[right])
                    right -=1
                return "".join(s1)



if __name__ == '__main__':
    s = Solution()
    print "The reverse string is :" + str(s.reverseString('hello'))
