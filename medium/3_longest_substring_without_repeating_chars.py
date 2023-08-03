"""
https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        batch = set()
        l = r = 0
        n = len(s)
        ans = 0
        while r < n:
            if s[r] not in batch:
                batch.add(s[r])
                ans = max(ans,len(batch))
            else:
                while l < r and s[l] != s[r]:
                    batch.remove(s[l])
                    l += 1
                l += 1
            r += 1
        return ans
