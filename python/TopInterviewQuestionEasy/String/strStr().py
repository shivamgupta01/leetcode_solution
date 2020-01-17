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
        if len(needle) == 0: return 0
        if len(haystack) == 0: return -1
        if len(needle) > len(haystack): return -1
        if haystack[0] == needle[0]: return 0
        i = 0
        start = needle[0]
        end = needle[-1]
        while i < len(haystack) - len(needle) + 1:
            if haystack[i] == start and haystack[i + len(needle)-1] == end:
                j = i
                start_needle = 0
                flag = True
                while j < i + len(needle):
                    if haystack[j] == needle[start_needle]:
                        j, start_needle = j + 1, start_needle + 1
                    else:
                        flag = False
                        break
                if flag: return i
            i += 1
        return -1

            
if __name__ == '__main__':
    s = Solution()
    print(s.strStr("babba","bbb"))