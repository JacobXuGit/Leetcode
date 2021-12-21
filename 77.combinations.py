#
# @lc app=leetcode id=77 lang=python3
#
# [77] Combinations
#

# @lc code=start
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        stack = collections.deque()
        stack.append((1, []))
        res = []
        while stack:
            print(stack)
            level, comb = stack.popleft()
            
            if len(comb) == k:
                res.append(comb)
                continue
            for i in range(level, n+1):
                stack.append((i+1, comb+[i]))

        return res

        

# @lc code=end

