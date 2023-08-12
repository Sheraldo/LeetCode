"""
https://leetcode.com/problems/add-two-numbers-ii/description/

Input: l1 = [7,2,4,3], l2 = [5,6,4]
Output: [7,8,0,7]

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [8,0,7]

Input: l1 = [0], l2 = [0]
Output: [0]
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseLL(self, l:Optional[ListNode]) -> Optional[ListNode]:
        rh = None
        while l is not None:
            c = l
            l = l.next
            c.next = None
            c.next = rh
            rh = c
        return rh

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        rev1, rev2 = self.reverseLL(l1), self.reverseLL(l2)
        ans = None
        carry = 0
        while rev1 or rev2 or carry:
            s = rev1.val if rev1 else 0
            s += rev2.val if rev2 else 0
            s += carry
            c = ListNode(s%10)
            carry = s//10
            c.next = ans
            ans = c
            if rev1: rev1 = rev1.next
            if rev2: rev2 = rev2.next
        return ans

