class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        verticalfreq = {}
        horizontalfreq = {}
        gridfreq1 = {}
        gridfreq2 = {}
        gridfreq3 = {}
        for i, x in enumerate(board):
            for j, y in enumerate(board[i]):
                if y == ".":
                    continue
                horizontalfreq[y] = horizontalfreq.get(y, 0) + 1
                if j < 3:
                    gridfreq1[y] = gridfreq1.get(y, 0) + 1
                    if gridfreq1[y] > 1:
                        return False
                elif j>=3 and j<6:
                    gridfreq2[y] = gridfreq2.get(y, 0) + 1
                    if gridfreq2[y] > 1:
                        return False
                else:
                    gridfreq3[y] = gridfreq3.get(y, 0) + 1
                    if gridfreq3[y] > 1:
                        return False
                if horizontalfreq[y] > 1:
                    return False
            horizontalfreq = {}
            if (i+1)%3 == 0:
                gridfreq1 = {}
                gridfreq2 = {}
                gridfreq3 = {}

        for j in range(0, 8):
            for i in range(0, 9):
                if board[i][j] == ".":
                    continue
                verticalfreq[board[i][j]] = verticalfreq.get(board[i][j], 0) + 1
                if verticalfreq[board[i][j]] > 1:
                    return False
            verticalfreq = {}

        return True