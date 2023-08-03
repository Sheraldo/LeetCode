"""
https://leetcode.com/problems/powx-n/description/

Input: x = 2.00000, n = 10
Output: 1024.00000

Input: x = 2.10000, n = 3
Output: 9.26100

Input: x = 2.00000, n = -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25
"""
import math
class Solution:
    def myPow(self, x: float, n: int) -> float:
        # print(f'{x=} , {n=}')
        if math.isclose(x,0.0):
            return 0.0
        elif n == 0:
            return 1.0
        elif n == -1:
            return 1/x
        
        if n&1:
            t = x
        else:
            t = 1
        t1 = self.myPow(x,n//2)
        return t1*t1*t
