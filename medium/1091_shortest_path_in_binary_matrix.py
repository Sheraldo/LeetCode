"""
https://leetcode.com/problems/shortest-path-in-binary-matrix/description/?envType=daily-question&envId=2023-09-06

Input: grid = [[0,1],[1,0]]
Output: 2

Input: grid = [[0,0,0],[1,1,0],[1,1,0]]
Output: 4

Input: grid = [[1,0,0],[1,1,0],[1,1,0]]
Output: -1
"""
dirs = ((0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1))
def is_valid_cell(grid, i, j):
    return i >= 0 and i<len(grid) and j>=0 and j<len(grid) and grid[i][j] == 0

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] or grid[-1][-1]:
            return -1
        q = deque()
        q.append((0, 0, 1))
        dp = [[False]*len(grid) for _ in range(len(grid))]
        dp[0][0] = True
        while q:
            n = len(q)
            for _ in range(n):
                i, j, zeros = q.popleft()
                if i == len(grid)-1 and j==len(grid)-1:
                    return zeros
                for d in dirs:
                    ni = i + d[0]
                    nj = j + d[1]
                    if is_valid_cell(grid, ni, nj) and not dp[ni][nj]:
                        dp[ni][nj] = True
                        q.append((ni, nj, zeros + 1))
        return -1

