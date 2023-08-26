"""
https://leetcode.com/problems/ransom-note/description/

Input: ransomNote = "a", magazine = "b"
Output: false

Input: ransomNote = "aa", magazine = "ab"
Output: false

Input: ransomNote = "aa", magazine = "aab"
Output: true
"""
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magCnt = Counter(magazine)
        rsntCnt = Counter(ransomNote)

        for c, cnt in rsntCnt.items():
            if c not in magCnt: return False
            if cnt > magCnt[c]: return False
        return True
