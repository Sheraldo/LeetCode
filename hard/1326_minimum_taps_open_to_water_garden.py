"""
https://leetcode.com/problems/minimum-number-of-taps-to-open-to-water-a-garden/description/

Input: n = 5, ranges = [3,4,1,1,0,0]
Output: 1
Explanation: The tap at point 0 can cover the interval [-3,3]
The tap at point 1 can cover the interval [-3,5]
The tap at point 2 can cover the interval [1,3]
The tap at point 3 can cover the interval [2,4]
The tap at point 4 can cover the interval [4,4]
The tap at point 5 can cover the interval [5,5]
Opening Only the second tap will water the whole garden [0,5]

Input: n = 3, ranges = [0,0,0,0]
Output: -1
Explanation: Even if you activate all the four taps you cannot water the whole garden.
"""
class Solution:
    def minTaps(self, n: int, ranges: list) -> int:
        n = len(ranges) - 1

        #dp[i] represents minimum taps required to water till i
        # initialise cache with max value
        dp = [n+1] * (n + 1)

        # set the effects of 0th index
        dp[0] = 1
        nr = min(n, ranges[0])
        for i in range(1, nr + 1):
            dp[i] = 1
        
        for i in range(1, n + 1):
            nl = max(0, i-ranges[i])
            nr = min(n, i+ranges[i])
            if nl == 0:
                # if incoming tap reaches 0, results in disabling all previous taps
                for j in range(0, nr + 1):
                    dp[j] = 1
                continue
            else:
                for j in range(nl, nr + 1):
                    # min taps required to water till nl
                    # incoming tap takes care of rest i.e []nl to nr]
                    dp[j] = min(dp[j], 1 + dp[nl])
        
        return dp[n] if dp[n] != n+1 else -1

