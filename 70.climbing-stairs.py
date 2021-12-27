#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1: return 1
        climbArr = [0] * n
        climbArr[0], climbArr[1] = 1, 2
        for i in range(n):
            if climbArr[i] == 0:
                climbArr[i] = climbArr[i-1]+climbArr[i-2]
        return climbArr[-1]

# @lc code=end

