#
# @lc app=leetcode id=1647 lang=python3
#
# [1647] Minimum Deletions to Make Character Frequencies Unique
#

# @lc code=start
class Solution:
    def minDeletions(self, s: str) -> int:
        freqMap = {}
        unique = set()
        res = 0
        for char in s:
            if char in freqMap:
                freqMap[char] += 1
            else:
                freqMap[char] = 1
        for _, val in enumerate(freqMap.items()):
            while val in unique and val != 0:
                val -= 1
                res += 1
            unique.add(val)
        return res

# @lc code=end

