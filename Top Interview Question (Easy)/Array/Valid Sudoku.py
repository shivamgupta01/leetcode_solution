class Solution(object):
    def isValidSudoku(self, board):


        i = 0
        while(i<9):
            temp = ['1','2','3','4','5','6','7','8','9']
            for val in board[i]:
                if val in temp:
                    temp.remove(val)
                elif val != '.':
                    return False


            i = i + 1

        i, j = 0, 0
        while (i < 9):
            j = 0
            temp = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
            while (j < 9):
                if board[j][i] in temp:
                    temp.remove(board[j][i])
                elif board[j][i] != '.':
                    return False
                j = j + 1
            i = i + 1


        temp = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        for i in range(0,3):
            for j in range(0,3):
                if board[i][j] in temp:
                    temp.remove(board[i][j])
                elif board[i][j] != '.':
                        return False

        temp = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        for i in range(0, 3):
            for j in range(3, 6):
                if board[i][j] in temp:
                    temp.remove(board[i][j])
                elif board[i][j] != '.':
                    return False

        temp = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        for i in range(0, 3):
            for j in range(6, 9):
                if board[i][j] in temp:
                    temp.remove(board[i][j])
                elif board[i][j] != '.':
                    return False






        temp = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        for i in range(3, 6):
            for j in range(0, 3):
                print board[i][j]
                if board[i][j] in temp:
                    temp.remove(board[i][j])
                elif board[i][j] != '.':
                    return False


        temp = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        for i in range(3, 6):
            for j in range(3, 6):
                if board[i][j] in temp:
                    temp.remove(board[i][j])
                elif board[i][j] != '.':
                    return False

        temp = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        for i in range(3, 6):
            for j in range(6, 9):
                if board[i][j] in temp:
                    temp.remove(board[i][j])
                elif board[i][j] != '.':
                    return False

        temp = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        for i in range(6, 9):
            for j in range(0, 3):
                if board[i][j] in temp:
                    temp.remove(board[i][j])
                elif board[i][j] != '.':
                    return False


        temp = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        for i in range(6, 9):
            for j in range(3, 6):
                if board[i][j] in temp:
                    temp.remove(board[i][j])
                elif board[i][j] != '.':
                    return False

        temp = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        for i in range(6, 9):
            for j in range(6, 9):
                if board[i][j] in temp:
                    temp.remove(board[i][j])
                elif board[i][j] != '.':
                    return False


        return True


if __name__ == '__main__':
    s = Solution()
    # print "Solution : " + str(s.isValidSudoku(
    #     [[".", "8", "9", "6", "5", "4", "3", "2", "1"],
    #      ["2", ".", ".", ".", ".", ".", ".", ".", "."],
    #      ["3", ".", ".", ".", ".", ".", ".", ".", "."],
    #      ["4", ".", ".", ".", ".", ".", ".", ".", "."],
    #      ["5", ".", ".", ".", ".", ".", ".", ".", "."],
    #      ["6", ".", ".", ".", ".", ".", ".", ".", "."],
    #      ["7", ".", ".", ".", ".", ".", ".", ".", "."],
    #      ["8", ".", ".", ".", ".", ".", ".", ".", "."],
    #      ["9", ".", ".", ".", ".", ".", ".", ".", "."]]))

    print  "Solution : " + str(s.isValidSudoku( [["9",".",".","6",".",".",".",".","."],
                                                 [".",".",".",".","6",".",".",".","."],
                                                 [".",".",".",".",".","1",".","3","."],
                                                 [".",".",".",".",".",".",".",".","8"],
                                                 [".",".",".",".",".","8",".",".","."],
                                                 [".",".",".","4",".",".","2",".","."],
                                                 [".",".",".",".",".",".",".",".","1"],
                                                 ["6",".",".",".","1",".",".",".","."],
                                                 [".",".",".",".",".",".",".",".","."]]
))

