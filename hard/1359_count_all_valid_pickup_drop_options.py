"""
https://leetcode.com/problems/count-all-valid-pickup-and-delivery-options/description/?envType=daily-question&envId=2023-09-10

Input: n = 1
Output: 1
Explanation: Unique order (P1, D1), Delivery 1 always is after of Pickup 1.

Input: n = 2
Output: 6
Explanation: All possible orders:
(P1,P2,D1,D2), (P1,P2,D2,D1), (P1,D1,P2,D2), (P2,P1,D1,D2), (P2,P1,D2,D1) and (P2,D2,P1,D1).
This is an invalid order (P1,D2,P2,D1) because Pickup 2 is after of Delivery 2.

Input: n = 3
Output: 90
"""
class Solution:
    def countOrders(self, n: int) -> int:
        dp = {}
        dp[(1,0)]=1
        dp[(0,1)]=1
        mod = int(1e9+7)
        def ways(p, d, dp):
            if (p, d) in dp:
                return dp[(p, d)]
            cnt = 0
            if p > 0:
                cnt = (cnt + p * ways(p-1, d+1, dp))%mod
            if d > 0:
                cnt = (cnt + d * ways(p, d-1, dp))%mod
            dp[(p, d)] = cnt
            return dp[(p, d)]
        return ways(n, 0, dp)

