# Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

# Example 1:

# Input: 121
# Output: true
# Example 2:

# Input: -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
# Example 3:

# Input: 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.


class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # Without Converting int to string
        # if x < 0 :
        #     return False
        # else:
        #     temp = []
        #     count = 0
        #     while x != 0:
        #         temp.append(x%10)
        #         x = int(x/10)
        #         count = count +1
        #     i = 0
        #     j = count -1
        #     print(temp)
        #     print(count)
        #     while i<j:
        #         if temp[i]!=temp[j]:
        #             return False
        #         i = i +1
        #         j = j -1
        #     return True

        # With Converting Int to String.
        # temp = (str(x))
        # i = 0
        # j = len(temp) -1


        # while i<j:
        #     if temp[i] != temp[j]:
        #         return False
        #     i = i + 1
        #     j = j - 1
        # return True

        # Time Complexity o(log N)

        if (x<0 or (x%10 == 0 and x !=0)):
            return False
        temp = 0 
        while (x>temp):
            temp = temp * 10 + x % 10
            x = int(x /10)
        print(temp)
        print(x)
        return x == temp or  x == int(temp/10)


if __name__ == '__main__':
    s = Solution()
    print(s.isPalindrome(121))