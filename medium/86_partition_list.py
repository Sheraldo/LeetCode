"""
https://leetcode.com/problems/partition-list/description/

Input: head = [1,4,3,2,5,2], x = 3
Output: [1,2,2,4,3,5]

Input: head = [2,1], x = 2
Output: [1,2]
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummy_less, dummy_more = ListNode(), ListNode()
        c, cl, cm = head, dummy_less, dummy_more
        while c:
            if c.val >= x:
                n = c.next
                c.next = None
                cm.next = c
                cm = cm.next
            else:
                n = c.next
                c.next = None
                cl.next = c
                cl = cl.next
            c = n
        cl.next = dummy_more.next
        return dummy_less.next

