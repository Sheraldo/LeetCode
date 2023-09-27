"""
https://leetcode.com/problems/decoded-string-at-index/description/?envType=daily-question&envId=2023-09-27

Example 1:

Input: s = "leet2code3", k = 10
Output: "o"
Explanation: The decoded string is "leetleetcodeleetleetcodeleetleetcode".
The 10th letter in the string is "o".

Example 2:

Input: s = "ha22", k = 5
Output: "h"
Explanation: The decoded string is "hahahaha".
The 5th letter is "h".

Example 3:

Input: s = "a2345678999999999999999", k = 1
Output: "a"
Explanation: The decoded string is "a" repeated 8301530446056247680 times.
The 1st letter is "a".



Constraints:

    2 <= s.length <= 100
    s consists of lowercase English letters and digits 2 through 9.
    s starts with a letter.
    1 <= k <= 109
    It is guaranteed that k is less than or equal to the length of the decoded string.
    The decoded string is guaranteed to have less than 263 letters.

"""
class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        size = 0
        for i, c in enumerate(s):
            if c.isdigit():
                size *= int(c)
            else:
                size += 1

            if k <= size:
                break

        for c in s[i::-1]:
            if c.isdigit():
                size /= int(c)
                k %= size
            else:
                if k % size == 0:
                    return c
                size -= 1

