"""
https://leetcode.com/problems/binary-tree-right-side-view/description/

Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]

Input: root = [1,null,3]
Output: [1,3]

Input: root = []
Output: []
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        ans = []

        q = deque()
        q.append(root)

        while q:
            n = len(q)
            for i in range(n):
                c = q.popleft()
                if i==n-1:
                    ans.append(c.val)
                if c.left: q.append(c.left)
                if c.right: q.append(c.right)
        return ans

