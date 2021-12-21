#
# @lc app=leetcode id=695 lang=python3
#
# [695] Max Area of Island
#

# @lc code=start
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        self.maxArea = 0
        def dfs(r, c):
            if grid[r][c] != 1:
                return 0
            grid[r][c] = 2
            self.currArea += 1
            if r + 1 < row:
                dfs(r + 1, c)
            if c + 1 < col:
                dfs(r, c + 1)
            if r - 1 >= 0:
                dfs(r - 1, c)
            if c - 1 >= 0:
                dfs(r, c - 1)

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    self.currArea = 0
                    dfs(i, j)
                    self.maxArea = max(self.currArea, self.maxArea)
        return self.maxArea
            
# @lc code=end

