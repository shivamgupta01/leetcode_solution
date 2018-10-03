'''
Reverse bits of a given 32 bits unsigned integer.

Example:

Input: 43261596
Output: 964176192
Explanation: 43261596 represented in binary as 00000010100101000001111010011100, 
             return 964176192 represented in binary as 00111001011110000010100101000000.
Follow up:
If this function is called many times, how would you optimize it?
'''

class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        
        temp = []
        res = 0
        while n:
            if n % 2 == 0:
                temp.append(0)
            else:
                temp.append(1)
            n = n // 2
        i = len(temp) - 1
        while(i < 32):
            temp.append(0)
            i = i + 1
        i = 31
        j = 0
        while i > -1:
            if temp[i] == 1:
                res = res + 2**j
            i = i -1 
            j = j + 1
        return res            

s = Solution()
print(s.reverseBits(1))