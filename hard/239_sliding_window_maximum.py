"""
https://leetcode.com/problems/sliding-window-maximum/description/

Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation:
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7


Input: nums = [1], k = 1
Output: [1]
"""
import heapq
from collections import deque
class Solution:
    # using maxheap
    def maxSlidingWindowMaxH(self, nums: List[int], k: int) -> List[int]:
        maxh = [ (-x, -i) for i, x in enumerate(nums[:k-1])]
        heapq.heapify(maxh)
        l, r = 0, k-1
        ret = []
        while r < len(nums):
            while maxh and -maxh[0][1] < l:
                # popping elements that are possible max but out of window
                heapq.heappop(maxh)
            heapq.heappush(maxh, (-nums[r], -r))
            ret.append(-maxh[0][0])
            r += 1
            l += 1
        return ret

    # using deque
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l, r = 0, 0
        q = deque()
        ret = []

        while r<len(nums):
            while q and nums[q[-1]] < nums[r]: q.pop()
            q.append(r)

            if l > q[0]:
                q.popleft()

            if r+1 >= k:
                ret.append(nums[q[0]])
                l += 1
            r += 1
        return ret

