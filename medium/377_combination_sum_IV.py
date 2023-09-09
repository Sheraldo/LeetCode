"""
https://leetcode.com/problems/combination-sum-iv/description/?envType=daily-question&envId=2023-09-09

Input: nums = [1,2,3], target = 4
Output: 7
Explanation:
The possible combination ways are:
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)
Note that different sequences are counted as different combinations.

Input: nums = [9], target = 3
Output: 0
"""
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0 for _ in range(target + 1)]
        dp[0] = 1
        for total in range(1, target + 1):
            for n in nums:
                if total - n >= 0:
                    dp[total] += dp[total - n]
        return dp[total]
