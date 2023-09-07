"""
https://leetcode.com/problems/reverse-linked-list-ii/description/?envType=daily-question&envId=2023-09-07

Input: head = [1,2,3,4,5], left = 2, right = 4
Output: [1,4,3,2,5]

Input: head = [5], left = 1, right = 1
Output: [5]
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def reverseLL(h):
    rh = None
    rt = None
    while h:
        tmp = h
        h = h.next
        tmp.next = None
        if rt == None:
            rt = tmp
        tmp.next = rh
        rh = tmp
    return rh, rt
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head
        
        dummy_head = ListNode()
        dummy_head.next = head

        prev = dummy_head
        rhead = dummy_head

        while left:
            prev = rhead
            rhead = rhead.next
            left -= 1
            right -= 1
        
        rtail = rhead

        while right:
            rtail = rtail.next
            right -= 1

        remaining = rtail.next
        rtail.next = None
        revh, revt = reverseLL(rhead)
        prev.next = revh
        revt.next = remaining
        return dummy_head.next

