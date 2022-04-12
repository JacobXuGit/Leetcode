#
# @lc app=leetcode id=979 lang=python3
#
# [979] Distribute Coins in Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        def dfs(root):
            if not root:
                return 0
                
            leftCollect = dfs(root.left)
            rightCollect = dfs(root.right)
            self.ans += abs(leftCollect) + abs(rightCollect)
            return root.val - 1 + leftCollect + rightCollect
        dfs(root)
        return self.ans
# @lc code=end

