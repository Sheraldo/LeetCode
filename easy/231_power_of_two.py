"""
https://leetcode.com/problems/power-of-two/description/

Input: n = 1
Output: true
Explanation: 20 = 1

Input: n = 16
Output: true
Explanation: 24 = 16

Input: n = 3
Output: false

"""
pow2s = {2**x for x in range(31)}
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n in pow2s
