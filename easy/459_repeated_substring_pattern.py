"""
https://leetcode.com/problems/repeated-substring-pattern/description/

Input: s = "abab"
Output: true
Explanation: It is the substring "ab" twice.

Input: s = "aba"
Output: false

Input: s = "abcabcabcabc"
Output: true
Explanation: It is the substring "abc" four times or the substring "abcabc" twice.
"""
def lps(s: str, lpsa: list):
    n=len(s)
    for i in range(1,n):
        x=lpsa[i-1]
        while s[x] != s[i]:
            if x==0:
                x=-1
                break
            x = lpsa[x-1]
        lpsa[i] = x+1

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n=len(s)
        lpsa = [0] * len(s)
        lps(s, lpsa)
        return (lpsa[n-1] != 0) and (lpsa[n-1]%(n-lpsa[n-1])==0)
