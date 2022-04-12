#
# @lc app=leetcode id=1304 lang=python3
#
# [1304] Find N Unique Integers Sum up to Zero
#

# @lc code=start
class Solution:
    def sumZero(self, n: int) -> List[int]:
        res = []
        if n % 2 == 1:
            res.append(0)
        upcell = n//2 + 1
        for i in range(1, upcell):
            res.append(i)
            res.append(-i)
        return res
# @lc code=end

