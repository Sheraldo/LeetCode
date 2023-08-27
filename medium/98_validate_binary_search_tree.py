"""
https://leetcode.com/problems/validate-binary-search-tree/description/

Input: root = [2,1,3]
Output: true

Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isVal(r, mn, mx):
            if not r:
                return True
            elif r.val >=mx or r.val <= mn:
                return False
            else:
                return isVal(r.left, mn, r.val) and isVal(r.right, r.val, mx)
        
        return isVal(root, -float('inf'), float('inf'))

