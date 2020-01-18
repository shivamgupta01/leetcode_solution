'''

In an alien language, surprisingly they also use english lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.

Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the given words are sorted lexicographicaly in this alien language.

 

Example 1:

Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
Output: true
Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.
'''

class Solution:
    def isAlienSorted(self, words, order):

        # Convert Alphabets to Numbers
        order_dict = {}
        count = 1
        for i in order:
            order_dict[i] = count
            count += 1
        i = 0
        while i < len(words) - 1:
            j = 0 
            flag = False
            while (j in range(0, min(len(words[i]),len(words[i + 1])))):
                if order_dict[words[i][j]] == order_dict[words[i + 1][j]]:
                    j = j + 1
                    continue
                elif order_dict[words[i][j]] > order_dict[words[i + 1][j]]:
                    return False
                else: 
                    flag = True
                    break
                j = j + 1
            
            if (flag == False) and (len(words[i]) > len(words[i + 1])) : return False
            i = i + 1

        return True




if __name__ == '__main__':
    s = Solution()
    print(s.isAlienSorted(["word","world","row"],'worldabcefghijkmnpqstuvxyz'))
        