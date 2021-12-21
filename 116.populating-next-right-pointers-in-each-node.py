#
# @lc app=leetcode id=116 lang=python3
#
# [116] Populating Next Right Pointers in Each Node
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
from collections import deque
class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        head, level = root, 0
        queue = deque()
        queue.append(head)
        while queue:
            for i in range(len(queue) - 1):
                queue[i].next = queue[i+1].next
            queue[-1].next = None
            level = len(queue)
            for i in range(level):
                if queue[i].left:
                    queue.append(queue[i].left)
                if queue[i].right:
                    queue.append(queue[i].right)
                queue.popleft()
        return root

            



# @lc code=end

