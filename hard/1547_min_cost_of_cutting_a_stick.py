"""
https://leetcode.com/problems/minimum-cost-to-cut-a-stick/description/

Input: n = 7, cuts = [1,3,4,5]
Output: 16
Explanation: Using cuts order = [1, 3, 4, 5] as in the input leads to the following scenario:
The first cut is done to a rod of length 7 so the cost is 7. The second cut is done to a rod of length 6 (i.e. the second part of the first cut), the third is done to a rod of length 4 and the last cut is to a rod of length 3. The total cost is 7 + 6 + 4 + 3 = 20.
Rearranging the cuts to be [3, 5, 1, 4] for example will lead to a scenario with total cost = 16 (as shown in the example photo 7 + 4 + 3 + 2 = 16).

Input: n = 9, cuts = [5,6,1,4,2]
Output: 22
Explanation: If you try the given cuts ordering the cost will be 25.
There are much ordering with total cost <= 25, for example, the order [4, 6, 5, 2, 1] has total cost = 22 which is the minimum possible.
"""
class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        dp = {}

        def getMinCost(l, r):
            if r - l == 1: return 0

            if (l,r) in dp: return dp[(l, r)]

            res = float("inf")
            for c in cuts:
                if l < c < r:
                    res = min(res, r - l + getMinCost(l, c) + getMinCost(c, r))
            dp[(l,r)] = res = 0 if res == float("inf") else res
            return dp[(l,r)]

        return getMinCost(0, n)

