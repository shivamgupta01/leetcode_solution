# In MATLAB, there is a very useful function called 'reshape', which can reshape a matrix into a new one with different size but keep its original data.
#
# You're given a matrix represented by a two-dimensional array, and two positive integers r and c representing the row number and column number of the wanted reshaped matrix, respectively.
#
# The reshaped matrix need to be filled with all the elements of the original matrix in the same row-traversing order as they were.
#
# If the 'reshape' operation with given parameters is possible and legal, output the new reshaped matrix; Otherwise, output the original matrix.
#
# Example 1:
# Input:
# nums =
# [[1,2],
#  [3,4]]
# r = 1, c = 4
# Output:
# [[1,2,3,4]]
# Explanation:
# The row-traversing of nums is [1,2,3,4]. The new reshaped matrix is a 1 * 4 matrix, fill it row by row by using the previous list.
# Example 2:
# Input:
# nums =
# [[1,2],
#  [3,4]]
# r = 2, c = 4
# Output:
# [[1,2],
#  [3,4]]
# Explanation:
# There is no way to reshape a 2 * 2 matrix to a 2 * 4 matrix. So output the original matrix.
# Note:
# The height and width of the given matrix is in range [1, 100].
# The given r and c are all positive.


class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]

        """
        r_original=len(nums)
        c_original = len(nums[0])
        count_Expected = r * c
        count_nums = (c_original * r_original)

        print
        if count_nums != count_Expected:
            return nums
        elif r_original==r and c_original==c:
            return nums
        else:
            temp = []
            newMatrix = [[0 for x in range(c)] for y in range(r)]
            for i in nums:
                for q in i:
                    temp.append(q)
            i, k = 0, 0
            while (i < r):
                j = 0
                while (j < c):
                    newMatrix[i][j] = temp[k]
                    j = j + 1
                    k = k + 1
                i = i + 1
            return newMatrix


if __name__ == '__main__':
    s = Solution()
    print "the Reshaped matrix is : " +str(s.matrixReshape([[1,2],[3,4]],4,1))