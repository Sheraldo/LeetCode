"""
https://leetcode.com/problems/fair-distribution-of-cookies/?envType=daily-question&envId=2023-09-12

Input: cookies = [8,15,10,20,8], k = 2
Output: 31
Explanation: One optimal distribution is [8,15,8] and [10,20]
- The 1st child receives [8,15,8] which has a total of 8 + 15 + 8 = 31 cookies.
- The 2nd child receives [10,20] which has a total of 10 + 20 = 30 cookies.
The unfairness of the distribution is max(31,30) = 31.
It can be shown that there is no distribution with an unfairness less than 31.

Input: cookies = [6,1,3,2,2,4,1,2], k = 3
Output: 7
Explanation: One optimal distribution is [6,1], [3,2,2], and [4,1,2]
- The 1st child receives [6,1] which has a total of 6 + 1 = 7 cookies.
- The 2nd child receives [3,2,2] which has a total of 3 + 2 + 2 = 7 cookies.
- The 3rd child receives [4,1,2] which has a total of 4 + 1 + 2 = 7 cookies.
The unfairness of the distribution is max(7,7,7) = 7.
It can be shown that there is no distribution with an unfairness less than 7.

Constraints:

    2 <= cookies.length <= 8
    1 <= cookies[i] <= 105
    2 <= k <= cookies.length

"""
class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        ans = float('inf')        
        dist = [0] * k
        def traverse(i):
            nonlocal ans, dist

            if i == len(cookies):
                ans = min(ans, max(dist))
                return
            if max(dist) >= ans: return

            for j in range(k):
                dist[j] += cookies[i]
                traverse(i + 1)
                dist[j] -= cookies[i]
        traverse(0)
        return ans

