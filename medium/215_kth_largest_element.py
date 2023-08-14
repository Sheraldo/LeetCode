"""
https://leetcode.com/problems/kth-largest-element-in-an-array/description/

Input: nums = [3,2,1,5,6,4], k = 2
Output: 5

Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4

"""
import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        q = []
        for x in nums:
            heapq.heappush(q, -x)
            if len(q) > len(nums) - k + 1:
                heapq.heappop(q)
        return -heapq.heappop(q)
