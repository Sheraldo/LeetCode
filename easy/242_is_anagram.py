"""
Input: s = "anagram", t = "nagaram"
Output: true

Input: s = "rat", t = "car"
Output: false
"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ds = dict()
        dt = dict()
        for c in s:
            ds[c] = ds.get(c,0) + 1
        for c in t:
            dt[c] = dt.get(c,0) + 1
        if len(ds) != len(dt): return False

        for k,v in ds.items():
            if dt.get(k,-1) != v:
                return False
        return True
