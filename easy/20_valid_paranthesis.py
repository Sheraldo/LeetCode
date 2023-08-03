"""
https://leetcode.com/problems/valid-parentheses/description/

Input: s = "()"
Output: true

Input: s = "()[]{}"
Output: true

Input: s = "(]"
Output: false

Input: s = "]"
Output: false
"""

par = {'(':')', '{':'}', '[':']'}
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c in par:
                stack.append(c)
            else:
                if len(stack) == 0 or par.get(stack[-1]) != c:
                    return False
                else:
                    stack.pop()
        return len(stack) == 0
