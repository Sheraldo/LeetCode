"""
https://leetcode.com/problems/minimum-deletions-to-make-character-frequencies-unique/description/?envType=daily-question&envId=2023-09-12

Input: s = "aab"
Output: 0
Explanation: s is already

Input: s = "aaabbbcc"
Output: 2
Explanation: You can delete two 'b's resulting in the good string "aaabcc".
Another way it to delete one 'b' and one 'c' resulting in the good string "aaabbc".

Input: s = "ceabaacb"
Output: 2
Explanation: You can delete both 'c's resulting in the good string "eabaab".
Note that we only care about characters that are still in the string at the end (i.e. frequency of 0 is ignored).
"""
class Solution:
    def minDeletions(self, s: str) -> int:
        count = Counter(s)
        used_freq = set()
        ans = 0
        for f in count.values():
            while f>0 and f in used_freq:
                f -= 1
                ans += 1
            used_freq.add(f)
        return ans

