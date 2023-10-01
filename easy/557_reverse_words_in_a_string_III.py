"""
https://leetcode.com/problems/reverse-words-in-a-string-iii/

Example 1:

Input: s = "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"

Example 2:

Input: s = "God Ding"
Output: "doG gniD"



Constraints:

    1 <= s.length <= 5 * 104
    s contains printable ASCII characters.
    s does not contain any leading or trailing spaces.
    There is at least one word in s.
    All the words in s are separated by a single space.

"""
class Solution:
    def reverseWords(self, s: str) -> str:
        ans = []
        for w in s.split(' '):
            ans.append(w[::-1])
        return " ".join(ans)

