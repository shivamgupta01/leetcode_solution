'''
The count-and-say sequence is the sequence of integers with the first five terms as following:

1.     1
2.     11
3.     21
4.     1211
5.     111221
1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.

Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the count-and-say sequence.

Note: Each term of the sequence of integers will be represented as a string.
'''

class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        # temp_ = {1:"1",2:"11",3:"21",4:"1211",5:"111221"}
        if n == 1:
            return '1'
        next_str = '1'
        for i in range(2,n+1):
            temp = ''
            j = 0
            k = j + 1
            count = 1
            while k < len(next_str):
                while k < len(next_str) and next_str[j] == next_str[k]:
                    count = count +1
                    k = k +1
                if k == len(next_str):
                    break
                temp = temp + str(count) + next_str[j]
                count = 1
                j = k
                k = k + 1
            if k == len(next_str):
            temp = temp + str(count) + next_str[j]
            else:
                temp = temp + '1' + next_str[-1]
            next_str = temp
        return next_str
            
                    

if __name__ == '__main__':
    s = Solution()
    print(s.countAndSay(3))