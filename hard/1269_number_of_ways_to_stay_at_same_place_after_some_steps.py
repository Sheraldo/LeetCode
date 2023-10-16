"""
https://leetcode.com/problems/number-of-ways-to-stay-in-the-same-place-after-some-steps/?envType=daily-question&envId=2023-10-15

Example 1:

Input: steps = 3, arrLen = 2
Output: 4
Explanation: There are 4 differents ways to stay at index 0 after 3 steps.
Right, Left, Stay
Stay, Right, Left
Right, Stay, Left
Stay, Stay, Stay

Example 2:

Input: steps = 2, arrLen = 4
Output: 2
Explanation: There are 2 differents ways to stay at index 0 after 2 steps
Right, Left
Stay, Stay

Example 3:

Input: steps = 4, arrLen = 2
Output: 8



Constraints:

    1 <= steps <= 500
    1 <= arrLen <= 106

"""
class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        
        dp = {}
        mod = int(1e9+7)

        def rec(i, steps_remaining):
            if i==arrLen or i<0: return 0
            if steps_remaining == 0:
                return 1 if i==0 else 0

            if (i, steps_remaining) not in dp:
                dp[(i, steps_remaining)] = (rec(i-1, steps_remaining - 1) +\
                                           rec(i, steps_remaining - 1) +\
                                           rec(i+1, steps_remaining - 1)) % mod
            
            return dp[(i, steps_remaining)]
        return rec(0, steps)

