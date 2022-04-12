#
# @lc app=leetcode id=289 lang=python3
#
# [289] Game of Life
#

# @lc code=start
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row, col = len(board), len(board[0])
        neighbors = [(1,0), (1,-1), (0,-1), (-1,-1), (-1,0), (-1,1), (0,1), (1,1)]

        for i in range(row):
            for j in range(col):

                liveNeighbors = 0
                for neighbor in neighbors:
                    x = i + neighbor[0]
                    y = j + neighbor[1]
                    if 0 <= x < row and 0 <= y < col and abs(board[x][y]) == 1:
                        liveNeighbors += 1
                
                if board[i][j] == 1 and (liveNeighbors < 2 or liveNeighbors > 3):
                    board[i][j] = -1
                if board[i][j] == 0 and liveNeighbors == 3:
                    board[i][j] = 2

        for i in range(row):
            for j in range(col):
                if board[i][j] == -1:
                    board[i][j] = 0
                if board[i][j] == 2:
                    board[i][j] = 1                    






        
# @lc code=end

