"""
https://leetcode.com/problems/reverse-integer/description/

Input: x = 123
Output: 321

Input: x = -123
Output: -321

Input: x = 120
Output: 21
"""
class Solution:
    def reverse(self, x: int) -> int:
        n = x
        rev = 0
        sign = -1 if x<0 else 1
        if n<0: n = n * -1
        
        while n>0:
            rev = rev*10 + n%10
            n = n//10
        
        if rev > 2**31: rev = 0
        rev = sign * rev
        return rev
