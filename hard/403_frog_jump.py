"""
https://leetcode.com/problems/frog-jump/description/

Input: stones = [0,1,3,5,6,8,12,17]
Output: true
Explanation: The frog can jump to the last stone by jumping 1 unit to the 2nd stone, then 2 units to the 3rd stone, then 2 units to the 4th stone, then 3 units to the 6th stone, 4 units to the 7th stone, and 5 units to the 8th stone.

Input: stones = [0,1,2,3,4,8,9,11]
Output: false
Explanation: There is no way to jump to the last stone as the gap between the 5th and 6th stone is too large.
"""
def progress(stones_pos, pos, dst, prev_jump, dp):
    idx = stones_pos[pos]
    if dp[idx][prev_jump] != -1:
        return dp[idx][prev_jump]
    if pos == dst:
        dp[idx][prev_jump] = True
        return dp[idx][prev_jump]
    
    dp[idx][prev_jump] = False
    for j in range(prev_jump-1, prev_jump+2):
        if j >= 0 and pos+j in stones_pos:
            dp[idx][prev_jump] |= progress(stones_pos, pos+j, dst, j, dp)
    return dp[idx][prev_jump]

class Solution:
    def canCross(self, stones: list) -> bool:
        # n is number of stones in list
        # max jump len can be n + 1
        if stones[1] > 1:
            # since 1st jump is 1 if stones[1] > 1, frog cannot jump further
            return False
        n = len(stones)
        dp = [[-1] * (n+1) for _ in range(n + 1)]
        for i in range(n+1):
            # reaching beyong n-1 with previous jump being i
            dp[n][i] = False
        stones_pos = {}
        for i, pos in enumerate(stones):
            stones_pos[pos] = i
        return progress(stones_pos, 1, stones[n-1], 1, dp)

