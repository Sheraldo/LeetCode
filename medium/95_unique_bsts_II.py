"""
https://leetcode.com/problems/unique-binary-search-trees-ii/description/

Input: n = 3
Output: [[1,null,2,null,3],[1,null,3,2],[2,1,3],[3,1,null,null,2],[3,2,null,1]]

Input: n = 1
Output: [[1]]
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        
        def genBST(s, e):
            if s > e: return [None]
            if s == e: return [TreeNode(s)]
            else:
                ans = []
                for i in range(s,e+1):
                    lset = genBST(s,i-1)
                    rset = genBST(i+1,e)
                    for l in lset:
                        for r in rset:
                            ch = TreeNode(i)
                            ch.left = l
                            ch.right = r
                            ans.append(ch)
                return ans
        
        return genBST(1,n)
