'''
Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2
Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1
Clarification:

What should we return when needle is an empty string? This is a great question to ask during an interview.

For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().
'''

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if len(needle) == 0:
            return 0
        else:
            i = 0
            while i <=len(haystack)-len(needle):
                x = i
                flag = True
                if haystack[x] == needle[0]:
                    for j in range(1,len(needle)):
                        x = x +1
                        if haystack[x] != needle[j]:
                            flag = False
                            break
                    if flag == True:
                        return i
                else:
                    i = i +1
                    continue
                i = i +1
            return -1

            
if __name__ == '__main__':
    s = Solution()
    print(s.strStr("mississippi","issip"))