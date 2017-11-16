# Write a program that outputs the string representation of numbers from 1 to n.
#
# Example:
#
# n = 15,
#
# Return:
# [
#     "1",
#     "2",
#     "Fizz",
#     "4",
#     "Buzz",
#     "Fizz",
#     "7",
#     "8",
#     "Fizz",
#     "Buzz",
#     "11",
#     "Fizz",
#     "13",
#     "14",
#     "FizzBuzz"
# ]

class Solution(object):
    def fizzBuzz(self, n):

        i = 1
        result = []
        while (i<=n):
            if i %15 == 0:
                result.append('FizzBuzz')
            elif i%5 == 0:
                result.append('Buzz')
            elif i % 3 == 0:
                result.append('Fizz')
            else:
                result.append(str(i))
            i = i + 1
        return result

if __name__ == '__main__':
    s = Solution()
    print "The Output is : " + str(s.fizzBuzz(10))