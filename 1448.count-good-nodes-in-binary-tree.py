#
# @lc app=leetcode id=1448 lang=python3
#
# [1448] Count Good Nodes in Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
Thinking process for this problem:
whenever there is good node, the path from root to this node, the value of current node
is greater or equal to the maximum value of the entire path
so we store the maximum value we get when we go through each nodes
with that maximum we are able to identify current node is good node
or not.
time complexity is O(n)
space complexity is O(n) as well
'''
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(root, currMax):
            if not root:
                return 0

            maxVal = max(root.val, currMax)
            if root.val >= currMax:
                return 1 + dfs(root.left, maxVal) + dfs(root.right, maxVal)

            return dfs(root.left, maxVal) + dfs(root.right, maxVal)
        
        return dfs(root, root.val)
            
'''
#BFS solution
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        queue = collections.deque()
        if root: queue.append((root, root.val))
        goodNodes = 0
        while queue:
            node, currMax = queue.popleft()
            if node.val >= currMax:
                goodNodes += 1
            if node.left:
                queue.append((node.left, max(currMax, node.val)))
            if node.right:
                queue.append((node.right, max(currMax, node.val)))
    
        return goodNodes
'''
        
# @lc code=end

