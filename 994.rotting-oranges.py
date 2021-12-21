#
# @lc app=leetcode id=994 lang=python3
#
# [994] Rotting Oranges
#

# @lc code=start
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row, col, minute = len(grid), len(grid[0]), -1
        freshCount = 0
        rottenQueue = collections.deque()
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    freshCount += 1
                if grid[i][j] == 2:
                    rottenQueue.append((i, j))
        while rottenQueue:
            size = len(rottenQueue)
            
            for _ in range(size):
                i, j = rottenQueue.popleft()
                if i - 1 >= 0 and grid[i-1][j] == 1:
                    grid[i-1][j] = 2
                    rottenQueue.append((i-1, j))
                    freshCount -= 1
                if i + 1 < row and grid[i+1][j] == 1:
                    grid[i+1][j] = 2
                    rottenQueue.append((i+1, j))
                    freshCount -= 1
                if j - 1 >= 0 and grid[i][j-1] == 1:
                    grid[i][j-1] = 2
                    rottenQueue.append((i, j-1))
                    freshCount -= 1
                if j + 1 < col and grid[i][j+1] == 1:
                    grid[i][j+1] = 2
                    rottenQueue.append((i, j+1))
                    freshCount -= 1
            minute += 1
        
        return max(0, minute) if freshCount == 0 else -1
        



# @lc code=end

