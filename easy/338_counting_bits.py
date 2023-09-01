"""
https://leetcode.com/problems/counting-bits/description/?envType=daily-question&envId=2023-09-01



Input: n = 2
Output: [0,1,1]
Explanation:
0 --> 0
1 --> 1
2 --> 10


Input: n = 5
Output: [0,1,1,2,1,2]
Explanation:
0 --> 0
1 --> 1
2 --> 10
3 --> 11
4 --> 100
5 --> 101

Follow up:

    It is very easy to come up with a solution with a runtime of O(n log n). Can you do it in linear time O(n) and possibly in a single pass?
    Can you do it without using any built-in function (i.e., like __builtin_popcount in C++)?
"""
class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n+1)
        
        for i in range(1, n+1):
            dp [i] = dp[i//2] + (1 if i&1 else 0)
        return dp

