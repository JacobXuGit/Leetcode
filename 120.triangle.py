#
# @lc app=leetcode id=120 lang=python3
#
# [120] Triangle
'''
For this problem we use dynamic programming to solve
there are several cases to consider when we go into a new row
if it is the beginning row = 0 in the array
we simply add it with traingle[row-1][col] above
if it is in the end of current array
we add triangle [row-1][col-1] above
otherwise
we have traingle[row-1][col-1] or [row-1][col] 
finally combine cases we will have the answer for this question

dynamic programming:avoid recalculation after each layer computed
we store its computation result and keep going
'''
# @lc code=start
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        for i in range(1, len(triangle)):
            for j in range(i + 1):
                smallest = math.inf
                if j > 0:
                    smallest = triangle[i-1][j-1]
                if j < i:
                    smallest = min(smallest, triangle[i-1][j])
                triangle[i][j] += smallest
        return min(triangle[-1])

            
# @lc code=end

