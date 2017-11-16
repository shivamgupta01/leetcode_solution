# Example 1:
# Input: ["Hello", "Alaska", "Dad", "Peace"]
# Output: ["Alaska", "Dad"]
# Note:
# You may use one character in the keyboard more than once.
# You may assume the input string will only contain letters of alphabet.


class Solution(object):
    def findWords(self, words):
        my_list = ['eiopqrtuwy', 'adfghjkls', 'bcmnvxz']
        result = []
        for x in words:
            if all(i in my_list[0] for i in list(''.join(set(x.lower())))):
                result.append(x)
            if all(j in my_list[1] for j in list(''.join(set(x.lower())))):
                result.append(x)
            if all(k in my_list[2] for k in list(''.join(set(x.lower())))):
                result.append(x)

        return result

if __name__ == '__main__':
    s = Solution()
    print "the Words are : " + str(s.findWords(["Hello", "Alaska", "Dad", "Peace"]))
