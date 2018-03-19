# Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.
#
# Example 1:
# Input: "aba"
# Output: True
# Example 2:
# Input: "abca"
# Output: True
# Explanation: You could delete the character 'c'.
# Note:
# The string will only contain lowercase characters a-z. The maximum length of the string is 50000.



class Solution(object):
    def validPalindrome(self, s):
        i = 0
        flag = True
        j = len(s)-1
        while j>=i:
            if s[i]!=s[j]:
                print s[i],s[j]
                if  s[i]==s[j-1]:
                    if s[i+1] == s[j-2]:
                        j = j -1


            elif (s[i+1]==s[j]) and flag == True:
                    if s[i+2]==s[j-1]:
                        i = i +1


            else:
                    return False


            i+=1
            j-=1

        return True




if __name__ == '__main__':
    s = Solution()
    print "solution : " + str(s.validPalindrome("aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga"))