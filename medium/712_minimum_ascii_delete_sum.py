"""
https://leetcode.com/problems/minimum-ascii-delete-sum-for-two-strings/description/

Input: s1 = "sea", s2 = "eat"
Output: 231
Explanation: Deleting "s" from "sea" adds the ASCII value of "s" (115) to the sum.
Deleting "t" from "eat" adds 116 to the sum.
At the end, both strings are equal, and 115 + 116 = 231 is the minimum sum possible to achieve this.

Input: s1 = "delete", s2 = "leet"
Output: 403
Explanation: Deleting "dee" from "delete" to turn the string into "let",
adds 100[d] + 101[e] + 101[e] to the sum.
Deleting "e" from "leet" adds 101[e] to the sum.
At the end, both strings are equal to "let", and the answer is 100+101+101+101 = 403.
If instead we turned both strings into "lee" or "eet", we would get answers of 433 or 417, which are higher.
"""
def mDS(s1, i1, s2, i2, dp):
    if dp[i1][i2] != -1: return dp[i1][i2]
    if i1 == len(s1):
        dp[len(s1)][i2] = sum(ord(c) for c in s2[i2:])
        return dp[i1][i2]
    if i2 == len(s2):
        dp[i1][len(s2)] = sum(ord(c) for c in s1[i1:])
        return dp[i1][i2]
    
    if s1[i1] == s2[i2]:
        dp[i1][i2] = mDS(s1, i1 + 1, s2, i2 + 1, dp)
    else:
        dp[i1][i2] = min(ord(s1[i1]) + mDS(s1, i1+1, s2, i2, dp), 
                     ord(s2[i2]) + mDS(s1, i1, s2, i2+1, dp))
    return dp[i1][i2]

class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        dp = [[-1] * (len(s2) + 1) for _ in range(len(s1) + 1)]
        dp[len(s1)][len(s2)] = 0
        return mDS(s1, 0, s2, 0, dp)

