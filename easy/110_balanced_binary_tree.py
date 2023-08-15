"""
https://leetcode.com/problems/balanced-binary-tree/description/

Input: root = [3,9,20,null,null,15,7]
Output: true

Input: root = [1,2,2,3,3,null,null,4,4]
Output: false
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def getHeight(c):
    if not c: return True, 0
    if c and not c.left and not c.right: return True, 1
    l_bal, lh = getHeight(c.left)
    r_bal, rh = getHeight(c.right)
    if abs(lh-rh) > 1: return False, max(lh, rh) + 1
    if not l_bal or not r_bal: return False, max(lh, rh) + 1
    return True, max(lh,rh) + 1
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        is_balanced, height = getHeight(root)
        return is_balanced
