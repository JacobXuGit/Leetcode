#
# @lc app=leetcode id=784 lang=python3
#
# [784] Letter Case Permutation
#

# @lc code=start
class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        resList = list(s)
        ans = []
        def backTrack(start):
            ans.append("".join(resList))
            for i in range(start, len(resList)):
                if resList[i].isnumeric():
                    continue
                resList[i] = resList[i].swapcase()
                backTrack(i+1)
                resList[i] = resList[i].swapcase()
        
        backTrack(0)
        return ans


# @lc code=end

