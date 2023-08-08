"""
https://leetcode.com/problems/minimum-depth-of-binary-tree/description/

Input: root = [3,9,20,null,null,15,7]
Output: 2

Input: root = [2,null,3,null,4,null,5,null,6]
Output: 5
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        ans = int(1e5+1)
        def mD(c, d):
            nonlocal ans
            if not c.left and not c.right: ans = min(ans,d)
            if c.left: mD(c.left, d+1)
            if c.right: mD(c.right, d+1)
        mD(root,1)
        return ans
