class Solution(object):
    def isValidSudoku(self, board):
        # Defining Variable to hold each group.
        row_dict = [{} for i in range(0, 9)]
        column_dict = [{} for i in range(0, 9)]
        sub_regions_dict = [{} for i in range(0,9)]

        for i in range(0, 9):
            for j in range(0, 9):
                curr = board[i][j]
                if curr != '.':
                    sub_region = int(i/3)*3 + int(j/3)
                    if curr not in sub_regions_dict[sub_region]:
                        sub_regions_dict[sub_region][curr] = True
                    else:
                        print(row_dict, column_dict, sub_regions_dict)
                        return False
                    if curr not in row_dict[i]:
                        row_dict[i][curr] = True
                    else:
                        return False
                    if curr not in column_dict[j]:
                        column_dict[j][curr] = True
                    else:
                        return False

        return True


if __name__ == '__main__':
    s = Solution()
    print("Solution : " + str(s.isValidSudoku( [[".",".","4",".",".",".","6","3","."],
                                                [".",".",".",".",".",".",".",".","."],
                                                ["5",".",".",".",".",".",".","9","."],
                                                [".",".",".","5","6",".",".",".","."],
                                                ["4",".","3",".",".",".",".",".","1"],
                                                [".",".",".","7",".",".",".",".","."],
                                                [".",".",".","5",".",".",".",".","."],
                                                [".",".",".",".",".",".",".",".","."],
                                                [".",".",".",".",".",".",".",".","."]])
))

