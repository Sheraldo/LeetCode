"""
Example 1:

Input: s = "bcabc"
Output: "abc"

Example 2:

Input: s = "cbacdcbc"
Output: "acdb"



Constraints:

    1 <= s.length <= 104
    s consists of lowercase English letters.

"""
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last = {}
        for i, c in enumerate(s):
            last[c] = i
        
        stack = []
        vis = set()

        for i, c in enumerate(s):
            if c in vis: continue

            while stack and stack[-1] > c and last[stack[-1]] > i:
                vis.remove(stack.pop())
            
            vis.add(c)
            stack.append(c)
        
        return "".join(stack)

