"""
Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
Explanation: The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r

Input: word1 = "ab", word2 = "pqrs"
Output: "apbqrs"
Explanation: Notice that as word2 is longer, "rs" is appended to the end.
word1:  a   b 
word2:    p   q   r   s
merged: a p b q   r   s

Input: word1 = "abcd", word2 = "pq"
Output: "apbqcd"
Explanation: Notice that as word1 is longer, "cd" is appended to the end.
word1:  a   b   c   d
word2:    p   q 
merged: a p b q c   d
"""
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        p1 = p2 = 0
        n1, n2 = len(word1), len(word2)
        s = ""
        while p1 < n1 and p2 < n2:
            s = s + word1[p1] + word2[p2]
            p1 += 1
            p2 += 1
        while p1 < n1:
            s += word1[p1]
            p1 += 1
        while p2 < n2:
            s += word2[p2]
            p2 += 1
        return s
