"""
https://leetcode.com/problems/path-with-minimum-effort/description/?envType=daily-question&envId=2023-09-16

Input: heights = [[1,2,2],[3,8,2],[5,3,5]]
Output: 2
Explanation: The route of [1,3,5,3,5] has a maximum absolute difference of 2 in consecutive cells.
This is better than the route of [1,2,2,2,5], where the maximum absolute difference is 3.

Input: heights = [[1,2,3],[3,8,4],[5,3,5]]
Output: 1
Explanation: The route of [1,2,3,4,5] has a maximum absolute difference of 1 in consecutive cells, which is better than route [1,3,5,3,5].

Input: heights = [[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]
Output: 0
Explanation: This route does not require any effort.
"""
dirs = ((0, 1), (1, 0), (0, -1), (-1, 0))

def is_valid(x, y, n, m):
    return x>=0 and y>=0 and x<n and y<m

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        n = len(heights)
        m = len(heights[0])
        dp = [[float('inf')] * m for _ in range(n)]

        dp[0][0] = 0

        min_heap = [(0, 0, 0)]

        while min_heap:
            effort, r, c = heappop(min_heap)
            if r == n-1 and c == m-1:
                break
            for dx, dy in dirs:
                nr = r + dx
                nc = c + dy
                if not is_valid(nr, nc, n, m):
                    continue
                n_effort = max(effort, abs(heights[r][c] - heights[nr][nc]))
                if n_effort < dp[nr][nc]:
                    dp[nr][nc] = n_effort
                    heappush(min_heap, (n_effort, nr, nc))
        return dp[n-1][m-1]

