"""
https://leetcode.com/problems/longest-palindromic-substring/description/

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Input: s = "cbbd"
Output: "bb"

"""
class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_l = 1
        max_idx = (0,0)
        for i in range(len(s)):
            # i as mid for odd len pal strings
            l = i
            r = i
            while l>=0 and r<len(s) and s[l]==s[r]:
                if r - l + 1 > max_l:
                    max_l = r - l + 1
                    max_idx = (l,r)

                l -= 1
                r += 1
            
        for i in range(len(s)-1):
            # i as mid for even len pal strings
            l = i
            r = i+1
            while l>=0 and r<len(s) and s[l]==s[r]:
                if r - l + 1 > max_l:
                    max_l = r - l + 1
                    max_idx = (l,r)
                l -= 1
                r += 1
        return s[max_idx[0]:max_idx[1]+1]
