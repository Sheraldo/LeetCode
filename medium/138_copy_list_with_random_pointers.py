"""
https://leetcode.com/problems/copy-list-with-random-pointer/description/?envType=daily-question&envId=2023-09-05

Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]

Input: head = [[1,1],[2,1]]
Output: [[1,1],[2,1]]

Input: head = [[3,null],[3,0],[3,null]]
Output: [[3,null],[3,0],[3,null]]
"""
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        c = head
        ans = Node(-1)
        ca = ans
        old_new_map = {}
        while c:
            ca.next = Node(c.val)
            old_new_map[c] = ca.next
            c = c.next
            ca = ca.next
        c = head
        while c:
            old_new_map[c].random = old_new_map[c.random] if c.random else None
            c = c.next
        return ans.next

