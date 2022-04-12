#
# @lc app=leetcode id=1822 lang=python3
#
# [1822] Sign of the Product of an Array
#

# @lc code=start
class Solution:
    def arraySign(self, nums: List[int]) -> int:
        ans = 1
        for num in nums:
            if num == 0:
                return 0
            elif num < 0:
                ans = -1 * ans
        return ans 
# @lc code=end

