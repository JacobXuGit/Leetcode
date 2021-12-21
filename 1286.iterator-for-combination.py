#
# @lc app=leetcode id=1286 lang=python3
#
# [1286] Iterator for Combination
#
from collections import deque
# @lc code=start
class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.characters = characters
        self.combinationLength = combinationLength
        self.queue = deque()
        self.dfs(self.characters, self.combinationLength, [], 0)
        
    def dfs(self, characters, maxLen, currStr, currPos):
        if maxLen == 0:
            self.queue.append("".join(currStr))
            return
        for i in range(currPos, len(self.characters)):
            currStr.append(characters[i])
            self.dfs(characters, maxLen - 1, currStr, i+1)
            currStr.pop()
    

    def next(self) -> str:
        return self.queue.popleft()

    def hasNext(self) -> bool:
        return len(self.queue)


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()
# @lc code=end

