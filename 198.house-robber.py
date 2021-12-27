#
# @lc app=leetcode id=198 lang=python3
#
# [198] House Robber
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        first, second = nums[0], max(nums[0], nums[1])
        for i in range(2, len(nums)):
            third = second
            if first + nums[i] > second:
                third =  first + nums[i]
            first = second
            second = third
        return max(first, second)

# @lc code=end

