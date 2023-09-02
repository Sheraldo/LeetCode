"""
https://leetcode.com/problems/extra-characters-in-a-string/description/?envType=daily-question&envId=2023-09-02

Input: s = "leetscode", dictionary = ["leet","code","leetcode"]
Output: 1
Explanation: We can break s in two substrings: "leet" from index 0 to 3 and "code" from index 5 to 8. There is only 1 unused character (at index 4), so we return 1.

Input: s = "sayhelloworld", dictionary = ["hello","world"]
Output: 3
Explanation: We can break s in two substrings: "hello" from index 3 to 7 and "world" from index 8 to 12. The characters at indices 0, 1, 2 are not used in any substring and thus are considered as extra characters. Hence, we return 3.
"""
class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        # store chars if no words match to end and all are left
        #dp = [len(s) - i for i in range(len(s))]
        dp = [51] * len(s)

        def left(s, i, dictionary, dp):
            if i == len(s):
                return 0
            if dp[i] != 51:
                return dp[i]
            # we get a word in dictionary that matches from i
            for w in dictionary:
                if s[i:i + len(w)] == w:
                    dp[i] = min(dp[i], left(s, i + len(w), dictionary, dp))
            # we don't try to match i
            dp[i] = min(dp[i], 1 + left(s, i+1, dictionary, dp))
            return dp[i]
        
        return left(s, 0, dictionary, dp)

