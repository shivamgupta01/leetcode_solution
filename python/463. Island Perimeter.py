class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        iIndex = 0
        numrows = len(grid) - 1
        numcols = len(grid[0]) - 1
        perimeter = 0
        for i in grid:
            jIndex = 0
            for j in i:
                if j == 1:
                    # code for Left check
                    if (jIndex - 1 < 0 or grid[iIndex][jIndex - 1] == 0):
                        perimeter = perimeter + 1
                    # code for Right check
                    if (jIndex + 1 > numcols or grid[iIndex][jIndex + 1] == 0):
                        perimeter = perimeter + 1
                    # code for Up check
                    if (iIndex - 1 < 0 or grid[iIndex - 1][jIndex] == 0):
                        perimeter = perimeter + 1
                    # code for Down check
                    if (iIndex + 1 > numrows or grid[iIndex + 1][jIndex] == 0):
                        perimeter = perimeter + 1
                jIndex = jIndex + 1

            iIndex = iIndex + 1

        return perimeter


if __name__ == '__main__':
    s = Solution();
    print "The perimeter is : " + str(s.islandPerimeter([[0, 1, 1], [0, 1, 0], [1, 1, 0]]))