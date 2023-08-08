"""
https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/
Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.

Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.
"""
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # obvious solution
        # return haystack.find(needle)
        combined = needle + '@' + haystack
        lpsa = [-1]*len(combined)

        def lps(s, arr):
            arr[0] = 0
            for i in range(1,len(combined)):
                x = arr[i-1]
                while s[x]!=s[i]:
                    if x==0:
                        x=-1
                        break
                    else:
                        x = lpsa[x-1]
                lpsa[i] = x + 1
        
        lps(combined,lpsa)

        for i in range(len(combined)):
            if lpsa[i] == len(needle):
                return i - 2*len(needle)
        
        return -1

