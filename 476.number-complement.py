#
# @lc app=leetcode id=476 lang=python3
#
# [476] Number Complement
#
# thoughts:
# the idea is to use the highest bit of given number
# propagate and or it from 1 to 2 to 4 to 8 to 16
# finally we get a bit mask with same length as the given num
# @lc code=start
class Solution:
    def findComplement(self, num: int) -> int:
        bitToGo, times = 1, num
        while times:
            num ^= bitToGo
            bitToGo = bitToGo << 1
            times = times >> 1
        return num
# @lc code=end

