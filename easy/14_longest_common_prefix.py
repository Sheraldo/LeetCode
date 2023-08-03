"""
https://leetcode.com/problems/longest-common-prefix/description/

Input: strs = ["flower","flow","flight"]
Output: "fl"

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

# This approach of using Trie is not optimal,
# you can use divide and conquer over 0,len(strs) -1 and return lcp for each partition

"""
class TrieNode:
    def __init__(self):
        self._children = {}
        self._EOW = False
        self._cnt = 0
class Trie:
    def __init__(self):
        self._root = TrieNode()
    
    def insert(self, s):
        curr = self._root
        curr._cnt += 1
        for c in s:
            curr = curr._children.setdefault(c,TrieNode())
            curr._cnt += 1
        curr._EOW = True
    def lcp(self, n):
        curr = self._root
        l = []
        while curr:
            nxt = None
            for c, curr_next in curr._children.items():
                if curr_next._cnt == n:
                    curr = curr_next
                    nxt = curr
                    l.append(c)
                    break
            if not nxt:
                break
        return "".join(l)


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        t = Trie()
        for s in strs:
            t.insert(s)
        return t.lcp(len(strs))
