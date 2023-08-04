"""
https://leetcode.com/problems/length-of-last-word/description/

Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.

Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.

Input: s = "luffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6.
"""
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.strip().split(' ')
        return len(words[-1])
