"""
Example 1:

Input: s = "abcd", t = "abcde"
Output: "e"
Explanation: 'e' is the letter that was added.

Example 2:

Input: s = "", t = "y"
Output: "y"



Constraints:

    0 <= s.length <= 1000
    t.length == s.length + 1
    s and t consist of lowercase English letters.

"""
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        tc = Counter(t)
        for c in s:
            tc[c] -= 1
            if tc[c] == 0: del tc[c]
        return list(tc.keys())[0]

