"""
https://leetcode.com/problems/palindrome-linked-list/description/

Input: head = [1,2,2,1]
Output: true

Input: head = [1,2]
Output: false

"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def findMid(h):
    s = f = h
    p=None
    l=0
    while f and f.next:
        p = s
        s = s.next
        f = f.next.next
        l += 2
    if f:
        l += 1
    return p,s,l
def reverseLL(l):
    rh = None
    while l:
        n = l.next
        l.next = None
        l.next = rh
        rh = l
        l = n
    return rh
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        prv, mid, l = findMid(head)
        if l==1: return True
        prv.next = None
        if l%2==0:
            rh = reverseLL(mid)
        else:
            rh = reverseLL(mid.next)
        
        p1, p2 = head, rh
        while p1 and p2:
            if p1.val != p2.val:
                return False
            p1 = p1.next
            p2 = p2.next
        if p1 or p2:
            return False
        return True

