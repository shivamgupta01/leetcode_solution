#   Valid Parentheses
# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#
# The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.



class Solution:
    def isValid(self,s):
        open_brackets=[]

        for i in s:

            if i =='(' or i =='{' or i == '[':
                open_brackets.append(i)
            elif i not in ['}',']',')']:
                continue
            elif len(open_brackets)>0:
                if (i == '}'and '{' ==  open_brackets[-1]) or \
                        (i == ')' and '(' == open_brackets[-1]) or\
                    (i == ']' and '[' == open_brackets[-1]) :
                    open_brackets.pop()
                else:
                    return False
            else:
                return False
        if len(open_brackets)>0:
            return False

        return True

if __name__ == '__main__':
    s = Solution()
    print "Solution : " + str(s.isValid('(:6;))()&&\'('))