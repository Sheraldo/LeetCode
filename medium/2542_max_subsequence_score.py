"""
https://leetcode.com/problems/maximum-subsequence-score/?envType=daily-question&envId=2023-09-12

Input: nums1 = [1,3,3,2], nums2 = [2,1,3,4], k = 3
Output: 12
Explanation:
The four possible subsequence scores are:
- We choose the indices 0, 1, and 2 with score = (1+3+3) * min(2,1,3) = 7.
- We choose the indices 0, 1, and 3 with score = (1+3+2) * min(2,1,4) = 6.
- We choose the indices 0, 2, and 3 with score = (1+3+2) * min(2,3,4) = 12.
- We choose the indices 1, 2, and 3 with score = (3+3+2) * min(1,3,4) = 8.
Therefore, we return the max score, which is 12.

Input: nums1 = [4,2,3,1,1], nums2 = [7,5,10,9,6], k = 1
Output: 30
Explanation:
Choosing index 2 is optimal: nums1[2] * nums2[2] = 3 * 10 = 30 is the maximum possible score.

Constraints:

    n == nums1.length == nums2.length
    1 <= n <= 105
    0 <= nums1[i], nums2[j] <= 105
    1 <= k <= n
"""
class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        sorted_nums2 = []
        for i, x in enumerate(nums2):
            sorted_nums2.append((x, i))
        sorted_nums2.sort(reverse=True)

        s = 0
        ans = float('-inf')
        min_heap = []

        for x, i in sorted_nums2:
            heappush(min_heap, nums1[i])
            s += nums1[i]
            if len(min_heap) > k:
                excluded = heappop(min_heap)
                s -= excluded
            if len(min_heap) == k:
                ans = max(s * x, ans)
        return ans

