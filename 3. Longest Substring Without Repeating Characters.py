"""

Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

"""


class Solution(object):
    def lengthOfLongestSubstring(self, s):
       i =0
       t = 0
       tempList = []
       countMax = []
       while (i<(len(s)-1)):
           tempList.append(s[i])
           temp = s[i + 1]
           print "adding element :" + s[i] + " to Temp List: " + str(tempList) + " index i = " + str(i)
           print "temp element is : " + s[i + 1] + " index = " + str(i + 1)
           i = i + 1
           for char in tempList:
               print "checking :" + char + " to : " + temp

               if char != temp:
                   print "in if condition"


               else:
                   print "in else loop ====================="
                   countMax.append(len(tempList))
                   print "appending : " + str(len(tempList)) + " to : " + str(countMax)
                   tempList = []
                   t = t + 1
                   i = t
                   print "i = " + str(i) +  " t = " + str(t)
                   break
       print str(countMax) + "=========="
       if len(countMax) == 0:
           return len(s)
       return max(countMax)


if __name__ == '__main__':
    s = Solution()
    print "the value of longest substring is : " + str(s.lengthOfLongestSubstring('abcabcbb'))





