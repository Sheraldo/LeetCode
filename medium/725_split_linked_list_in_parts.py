"""
https://leetcode.com/problems/split-linked-list-in-parts/description/?envType=daily-question&envId=2023-09-06

Input: head = [1,2,3], k = 5
Output: [[1],[2],[3],[],[]]
Explanation:
The first element output[0] has output[0].val = 1, output[0].next = null.
The last element output[4] is null, but its string representation as a ListNode is [].

Input: head = [1,2,3,4,5,6,7,8,9,10], k = 3
Output: [[1,2,3,4],[5,6,7],[8,9,10]]
Explanation:
The input has been split into consecutive parts with size difference at most 1, and earlier parts are a larger size than the later parts.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def getLen(c):
    count = 0
    while c:
        count += 1
        c = c.next
    return count

class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        l = getLen(head)
        counts = [l//k for _ in range(k)]
        for i in range(l%k):
            counts[i] += 1
        
        dummy_heads = [ListNode() for _ in range(k)]
        tail = [c for c in dummy_heads]
        tmp = None
        curr = head

        for i in range(k):
            while counts[i]:
                if curr: 
                    tmp = curr
                    curr = curr.next
                    tmp.next = None
                else:
                    tmp = None
                    break
                tail[i].next = tmp
                tail[i] = tail[i].next
                counts[i] -= 1
        
        res = [c.next for c in dummy_heads]
        return res

