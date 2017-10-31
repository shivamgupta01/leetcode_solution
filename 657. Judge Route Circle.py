# Initially, there is a Robot at position (0, 0). Given a sequence of its moves, judge if this robot makes a circle, which means it moves back to the original place.
#
# The move sequence is represented by a string. And each move is represent by a character. The valid robot moves are R (Right), L (Left), U (Up) and D (down). The output should be true or false representing whether the robot makes a circle.
#
# Example 1:
# Input: "UD"
# Output: true
# Example 2:
# Input: "LL"
# Output: false


class Solution(object):
    def judgeCircle(self, moves):

        i = 0
        countL = 0
        countU = 0

        if len(moves) == 0:
            return True
        if len(moves) %2 !=0:
            return False
        while i<len(moves):
            if moves[i] == 'L':
                countL = countL + 1
            elif  moves[i] == 'R':
                countL = countL -1
            elif moves[i] == 'U':
                countU = countU + 1
            else:
                countU = countU -1
            i = i + 1
        if (countU == countL == 0 or countL  == countU):
            return True
        return False

if __name__ == '__main__':
    s= Solution()
    print "The Hamming Distance between numbers are: " + str(s.judgeCircle('DURDLDRRLL'))
