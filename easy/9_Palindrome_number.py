"""
https://leetcode.com/problems/palindrome-number/description/

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

"""
from collections import deque
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        num = x
        digits = deque()
        while num:
            digits.appendleft(num%10)
            num = num//10
        
        l = 0
        r = len(digits) - 1

        while l < r:
            if digits[l] != digits[r]:
                return False
            l += 1
            r -= 1
        return True
