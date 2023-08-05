"""
https://leetcode.com/problems/add-two-numbers/description/

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Input: l1 = [0], l2 = [0]
Output: [0]

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dh = ListNode()
        h = dh
        c = 0
        while l1 or l2 or c:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            cs = x + y + c
            h.next = ListNode(cs%10)
            c = cs//10
            h = h.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next
        return dh.next
