"""
https://leetcode.com/problems/longest-increasing-subsequence/description/

Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.

Input: nums = [0,1,0,3,2,3]
Output: 4

Input: nums = [7,7,7,7,7,7,7]
Output: 1
"""
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n

        for i in range(n-1, -1, -1):
            for j in range(i+1, n):
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)

