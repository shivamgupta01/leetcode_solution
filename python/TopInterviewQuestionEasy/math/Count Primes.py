'''
Count the number of prime numbers less than a non-negative number, n.

Example:

Input: 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
'''
import math
class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <3 :
            return 0
        temp = [True] * n
        temp[0] = False
        temp[1] = False
        i = 2
        while(i<math.sqrt(n)+1):
            k = 1
            if temp[i] == True and self.isPrime(i) == True:
                while i*k <len(temp):
                    temp[i * k] = False
                    k = k + 1
            i = i + 1
        return sum(temp)

    def isPrime(self,n):
        i =2
        while i<=math.sqrt(n):
            if n % i == 0:
                return False
            i = i + 1
        return True

s = Solution()
print(s.countPrimes(999983))
