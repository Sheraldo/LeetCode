"""
https://leetcode.com/problems/integer-break/?envType=daily-question&envId=2023-10-06

Example 1:

Input: n = 2
Output: 1
Explanation: 2 = 1 + 1, 1 × 1 = 1.

Example 2:

Input: n = 10
Output: 36
Explanation: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36.



Constraints:

    2 <= n <= 58
"""
class Solution:
    def integerBreak(self, n: int) -> int:
        dp = {1: 1}

        for x in range(2, n + 1):
            dp[x] = 0 if x==n else x
            for i in range(1, x):
                dp[x] = max(dp[x], dp[i]*dp[x-i])
        return dp[n]

        # def dfs(x):
        #     if x in dp: return dp[x]
        #     dp[x] = 0 if x == n else x
        #     for i in range(1, x):
        #         val = dfs(i) * dfs(x-i)
        #         dp[x] = max(dp[x], val)
        #     return dp[x]

        return dfs(n)

