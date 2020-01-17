'''
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
Note: You may assume the string contain only lowercase letters.
'''

import collections

class Solution():
    def firstUniqChar(self, s: str) -> int:
        # Original Solution
        # temp_dict = {}
        # for i in s:
        #     if i not in temp_dict:
        #         temp_dict[i] = True
        #     else:
        #         temp_dict[i] = False
        #
        # for i in range(0,len(s)):
        #     if s[i] in temp_dict and temp_dict[s[i]] == True:
        #         return i
        # return -1

        # Modified Solution
        temp_dict = collections.Counter(s)
        print(temp_dict)
        for key, val in temp_dict.items():
            if temp_dict[key] == 1:
                return s.index(key)
        return -1



if __name__ == '__main__':
    s=Solution()
    print(s.firstUniqChar("aadadaads"))