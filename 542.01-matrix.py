#
# @lc app=leetcode id=542 lang=python3
#
# [542] 01 Matrix
#

# @lc code=start
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        
        distance = [[None]*n for _ in repeat(None, m)]
        
        d = deque()
        
        for i in range(m):
            for j in range(n):
                if not mat[i][j]:
                    distance[i][j] = 0
                    d.append((i, j))
        
        while d:
            i, j = d.popleft()
            
            if i > 0 and distance[i-1][j] is None:
                distance[i-1][j] = distance[i][j] + 1
                d.append((i-1, j))
            if j < n-1 and distance[i][j+1] is None:
                distance[i][j+1] = distance[i][j] + 1
                d.append((i, j+1))
            if i < m-1 and distance[i+1][j] is None:
                distance[i+1][j] = distance[i][j] + 1
                d.append((i+1, j))
            if j > 0 and distance[i][j-1] is None:
                distance[i][j-1] = distance[i][j] + 1
                d.append((i, j-1))
            print(distance)
        return distance

        
        
    
# @lc code=end

