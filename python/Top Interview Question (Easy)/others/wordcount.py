import string
import collections
import operator

class Solution:

 def wordCount(self,nums):
    nums = "Hello, number of transaction which happened, for, bitcoin was about 490K in a single day. In order to read all these transaction we need to have highly scalable system supporting parallel processing architecture. The API will we plan to design should be highly scalable and reliable. It, should be able to handle much larger volume of transaction that the highest till date. "

    nums=nums.lower().translate(None,string.punctuation).split()
    d = {}
    for i in nums:
        if i not in d:
            d[i] = 1
        else:
            d[i] = d[i]+1


    sorted_d = (sorted(d.items(), key = operator.itemgetter(1), reverse=True))

    for key,val in sorted_d:
        print key,val



if __name__ == '__main__':
    s = Solution()
    s.wordCount("")
