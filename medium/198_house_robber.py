"""
https://leetcode.com/problems/house-robber/description/

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.

Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.
"""
class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0] * (len(nums) + 2)
        for i in range(len(nums) - 1, -1, -1):
            dp[i] = max(nums[i] + dp[i+2], dp[i+1])
        return dp[0]
