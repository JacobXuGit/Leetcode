#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#

# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        def backTrack(start):
            if start == len(nums):
                self.res.append(nums[:])
            for i in range(start, len(nums)):
                nums[start], nums[i] = nums[i], nums[start]
                backTrack(start+1)
                nums[start], nums[i] = nums[i], nums[start]
        backTrack(0)
        return self.res

            


# @lc code=end

