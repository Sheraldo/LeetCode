"""
https://leetcode.com/problems/minimum-penalty-for-a-shop/description/

Input: customers = "YYNY"
Output: 2
Explanation:
- Closing the shop at the 0th hour incurs in 1+1+0+1 = 3 penalty.
- Closing the shop at the 1st hour incurs in 0+1+0+1 = 2 penalty.
- Closing the shop at the 2nd hour incurs in 0+0+0+1 = 1 penalty.
- Closing the shop at the 3rd hour incurs in 0+0+1+1 = 2 penalty.
- Closing the shop at the 4th hour incurs in 0+0+1+0 = 1 penalty.
Closing the shop at 2nd or 4th hour gives a minimum penalty. Since 2 is earlier, the optimal closing time is 2.



Input: customers = "NNNNN"
Output: 0
Explanation: It is best to close the shop at the 0th hour as no customers arrive.

Input: customers = "YYYY"
Output: 4
Explanation: It is best to close the shop at the 4th hour as customers arrive at each hour.
"""
class Solution:
    def bestClosingTime(self, customers: str) -> int:
        n = len(customers)
        n_count = [0]*n
        y_count = [0]*n
        for i, stat in enumerate(customers):
            if stat == 'Y':
                y_count[i] = 1
            else:
                n_count[i] = 1
        
        for i in range(1, n):
            n_count[i] += n_count[i-1]
            y_count[i] += y_count[i-1]
        n_count.append(n_count[n-1])
        y_count.append(y_count[n-1])
        ans = n
        pen = float('inf')

        for i in range(n+1):
            # ith is chosen as closing hour
            n_before = n_count[i-1] if i>0 else 0
            y_after = y_count[n] if i==0 else y_count[n] - y_count[i-1]
            c_pen = n_before + y_after

            if c_pen < pen:
                ans = i
                pen = c_pen
        return ans

