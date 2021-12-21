#
# @lc app=leetcode id=733 lang=python3
#
# [733] Flood Fill
#

# @lc code=start
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        
        def bfs(image, sr, sc, newcolor, oldcolor):
            if sr >= len(image) or sr < 0:
                return
            if sc >= len(image[0]) or sc <0:
                return
            if image[sr][sc] == newcolor:
                return
            if image[sr][sc] == oldcolor:
                image[sr][sc] = newColor
            bfs(image, sr + 1, sc, newcolor, oldcolor)
            bfs(image, sr -1, sc, newcolor, oldcolor)
            bfs(image, sr, sc + 1, newcolor, oldcolor)
            bfs(image, sr, sc - 1, newcolor, oldcolor)
            return
        bfs(image, sr, sc, newcolor, image[sr][sc])
        return image
# @lc code=end

