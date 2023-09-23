"""
https://leetcode.com/problems/longest-string-chain/?envType=daily-question&envId=2023-09-23

Example 1:

Input: words = ["a","b","ba","bca","bda","bdca"]
Output: 4
Explanation: One of the longest word chains is ["a","ba","bda","bdca"].

Example 2:

Input: words = ["xbc","pcxbcf","xb","cxbc","pcxbc"]
Output: 5
Explanation: All the words can be put in a word chain ["xb", "xbc", "cxbc", "pcxbc", "pcxbcf"].

Example 3:

Input: words = ["abcd","dbqca"]
Output: 1
Explanation: The trivial word chain ["abcd"] is one of the longest word chains.
["abcd","dbqca"] is not a valid word chain because the ordering of the letters is changed.



Constraints:

    1 <= words.length <= 1000
    1 <= words[i].length <= 16
    words[i] only consists of lowercase English letters.

"""
from collections import defaultdict
class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        l_words = defaultdict(set)
        dp = {}
        for w in words:
            l_words[len(w)].add(w)
            dp[w] = None if len(w)>1 else 1
        
        def solve(word, l_words, dp):
            if dp[word] is not None:
                return dp[word]
            ans = 1
            for i in range(len(word)):
                c_word = word[:i] + word[i+1:]
                if c_word in l_words[len(c_word)]:
                    ans = max(ans, 1 + solve(c_word, l_words, dp))
            dp[word] = ans
            return dp[word]
        
        ans = 1
        for w in words:
            ans = max(ans, solve(w, l_words, dp))
        return ans

