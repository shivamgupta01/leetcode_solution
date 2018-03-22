class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """

        i = len(matrix) - 2
        j = 0
        if len(matrix)==1:
            return True
        while i != 0 or j != len(matrix[0]) - 1:
            temp = set()
            temp2 = 0
            while (i < len(matrix) and j<len(matrix[0])):
                temp.add(matrix[i][j])
                i = i + 1
                j = j + 1
                temp2 = temp2 + 1
            if len(temp) > 1:
                return False

            if i - temp2 - 1<0:
                i = 0
                j = j-temp2+1

            else:
                i = i - temp2 - 1
                j = 0

        return True

if __name__ == '__main__':
    s = Solution()
    print "the Solution is : " + str(s.isToeplitzMatrix([[1,2],
                                                         [5,2],
                                                         [9,5]]))

    #1,2,3,4
    #5,1,2,3
    #9,5,1,2