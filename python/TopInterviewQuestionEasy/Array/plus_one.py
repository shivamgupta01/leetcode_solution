"""
Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:

Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Example 2:

Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
"""

def plusOne(digits):
    """
    Plus 1 to integer.
    :param digits: List(int)
    :return: List(int)
    """
    len_digits = len(digits) - 1
    digits_to_int = 0
    for digit in digits:
        digits_to_int = digits_to_int + digit * (10 ** len_digits)
        len_digits = len_digits - 1
    return list(str(digits_to_int+1))


print(plusOne([9,9,8]))