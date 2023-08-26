"""
https://leetcode.com/problems/maximum-length-of-pair-chain/description/

Input: pairs = [[1,2],[2,3],[3,4]]
Output: 2
Explanation: The longest chain is [1,2] -> [3,4].

Input: pairs = [[1,2],[7,8],[4,5]]
Output: 3
Explanation: The longest chain is [1,2] -> [4,5] -> [7,8].

"""
class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda p: p[1])
        clen = 1
        cend = pairs[0][1]

        for i in range(1,len(pairs)):
            if cend < pairs[i][0]:
                clen += 1
                cend = pairs[i][1]
        return clen

