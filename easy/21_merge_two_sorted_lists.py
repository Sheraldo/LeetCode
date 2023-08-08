"""
https://leetcode.com/problems/merge-two-sorted-lists/description/

Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]


Input: list1 = [], list2 = []
Output: []

Input: list1 = [], list2 = [0]
Output: [0]
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dh = ListNode()
        c = dh
        h1 = list1
        h2 = list2
        while h1 and h2:
            if h1.val <= h2.val:
                c.next = h1
                h1 = h1.next
            else:
                c.next = h2
                h2 = h2.next
            c = c.next
        
        while h1:
            c.next = h1
            h1 = h1.next
            c = c.next
        
        while h2:
            c.next = h2
            h2 = h2.next
            c = c.next
        
        return dh.next
