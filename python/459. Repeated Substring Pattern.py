'''
Given a non-empty string check if it can be constructed by taking a substring of it and appending multiple copies of the substring together. You may assume the given string consists of lowercase English letters only and its length will not exceed 10000.

 

Example 1:

Input: "abab"
Output: True
Explanation: It's the substring "ab" twice.
Example 2:

Input: "aba"
Output: False
Example 3:

Input: "abcabcabc"
Output: True
Explanation: It's the substring "abc" four times. (And the substring "abcabc" twice.)
'''

class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        x = len(s)
        if x == 1:
            return False      
        divisor = int(x/2)
        while divisor > 0  :
            if x%divisor == 0:
                i = 0
                flag = True
                temp2 = divisor
                while temp2 < x:
                    if s[i:temp2] != s[temp2:temp2 +divisor]:
                        flag = False
                        break
                    i  = i + divisor
                    temp2 = temp2 + divisor
                if flag == False:
                    divisor -= 1
                    continue
                else:
                    return True
            divisor = divisor - 1
        return False


if __name__ == '__main__':
    s = Solution()
    print(s.repeatedSubstringPattern('bbb'))