#
# @lc app=leetcode id=1405 lang=python3
#
# [1405] Longest Happy String
#
import heapq
# @lc code=start
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        input = [(-a, "a"), (-b, "b"), (-c, "c")]
        heap = []
        for num, char in input:
            if num:
                heapq.heappush(heap, (num, char))
        res = ""
        while heap:
            num, char = heapq.heappop(heap)
            if len(res) > 1 and res[-1] == res[-2] == char:
                if not heap: break
                num, char = heapq.heapreplace(heap, (num, char))
            res += char
            if num + 1:
                heapq.heappush(heap, (num+1, char))
        return res
        

        
# @lc code=end

