#   Reverse Integer
# Given a 32-bit signed integer, reverse digits of an integer.
#
# Example 1:
#
# Input: 123
# Output:  321
# Example 2:
#
# Input: -123
# Output: -321
# Example 3:
#
# Input: 120
# Output: 21
# Note:
# Assume we are dealing with an environment which could only hold integers within the 32-bit signed integer range. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.



class Solution(object):
    def reverse(self, x):
        is_negative = False
        if x < 0:
            is_negative = True
        x = abs(x)
        int_list = []
        new_number = 0
        while x != 0:
            int_list.append(x%10)
            x = x // 10
        j = len(int_list) - 1
        for i in range(0, len(int_list)):
            add_to_num = 10 ** j * int_list[i]
            new_number = new_number + add_to_num
            j = j - 1
        if new_number > 2147483647 or new_number < -2147483648:
            return 0
        if is_negative:
            return -1 * new_number
        else:
            return new_number








if __name__ == '__main__':
    s=Solution()
    print("Solution is : " + str(s.reverse(1534236469)))