#   Valid Palindrome
# Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
#
# For example,
# "A man, a plan, a canal: Panama" is a palindrome.
# "race a car" is not a palindrome.
#
# Note:
# Have you consider that the string might be empty? This is a good question to ask during an interview.
#
# For the purpose of this problem, we define empty string as valid palindrome.






class Solution(object):
    def isPalindrome(self, s):
        start, end = 0, len(s)-1
        flag = True
        while(start < end and start < len(s) and end > 0):
            if s[start].isalnum() == False:
                start += 1
            elif s[end].isalnum() == False:
                end -= 1
            elif s[end].lower() != s[start].lower():
                flag = False
                start, end = start + 1, end - 1
            else:
                start, end = start + 1, end - 1
        return flag

if __name__ == '__main__':
    s = Solution()
    print("solutin : " + str(s.isPalindrome('A man, a plan, a canal: Panama')))





