"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minval = prices[0]
        maxP = 0
        for i in range(1,len(prices)):
            if minval < prices[i]:
                maxP = max(maxP, prices[i] - minval)
            else:
                minval = prices[i]
        return maxP
