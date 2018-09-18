'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
'''

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""
        elif len(strs) == 1:
            return strs[0]
        else:
            temp = strs[0]
            for i in range(1,len(strs)):
                if temp == strs[i]:
                    continue
                else:
                    index = 0
                    temp2 = ""
                    while index<len(strs[i]) and index<len(temp) and (strs[i][index] == temp[index]):
                        temp2 = temp2 + strs[i][index]
                        index = index + 1
                    
                    temp = temp2
                    if temp == '':
                        return ""
            if len(temp) != 0:
                return temp
            else:
                return ""
        


        
if __name__ == '__main__':
    s = Solution()
    print(s.longestCommonPrefix(["dog","racecar","car"]))