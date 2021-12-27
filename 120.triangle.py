#
# @lc app=leetcode id=120 lang=python3
#
# [120] Triangle
#

# @lc code=start
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = [[0 for _ in range(len(triangle))]for j in range(len(triangle[0]))]
        dp [0][0] = triangle[0][0]
        for i in range(len(triangle)-1):
            
# @lc code=end

