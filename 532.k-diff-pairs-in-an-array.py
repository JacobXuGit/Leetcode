#
# @lc app=leetcode id=532 lang=python3
#
# [532] K-diff Pairs in an Array
#

# @lc code=start
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        mapper, res = {}, 0
        for num in nums:
            if num in mapper:
                mapper[num] += 1
            else:
                mapper[num] = 1
        for key in mapper:
            if k > 0 and key + k in mapper:
                res += 1
            elif k == 0 and mapper[key+k] > 1:
                res += 1
        return res    


# @lc code=end

