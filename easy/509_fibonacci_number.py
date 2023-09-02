"""
https://leetcode.com/problems/fibonacci-number/description/

Input: n = 2
Output: 1
Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.

Input: n = 3
Output: 2
Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.

Input: n = 4
Output: 3
Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.
"""
class Solution:
    def fib(self, n: int) -> int:
        if n == 1 or n == 0:
            return n
        pn1, pn2 = 1, 0
        i = 2
        while i<=n:
            pn1, pn2 = pn1 + pn2, pn1
            i += 1
        return pn1

