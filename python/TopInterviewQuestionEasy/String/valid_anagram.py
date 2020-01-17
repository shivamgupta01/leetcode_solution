#   Valid Anagram
# Given two strings s and t, write a function to determine if t is an anagram of s.
#
# For example,
# s = "anagram", t = "nagaram", return true.
# s = "rat", t = "car", return false.
#
# Note:
# You may assume the string contains only lowercase alphabets.
#
# Follow up:
# What if the inputs contain unicode characters? How would you adapt your solution to such case?


import collections
class Solution(object):
    def isAnagram(self, s, t):
        # Original Solution
        # if len(s) != len(t):
        #     return False
        # temp_s = collections.Counter(s)
        # for i in t:
        #     if i not in temp_s:
        #         return False
        #     else:
        #         if temp_s[i] != 1:
        #             temp_s[i] = temp_s[i] - 1
        #         else:
        #             del temp_s[i]
        # return True

        # Counter Solution
        return collections.Counter(s) == collections.Counter(t)

if __name__ == '__main__':
    s = Solution()
    print("SOlution : " + str(s.isAnagram('ab','a')))