"""
https://leetcode.com/problems/01-matrix/description/

Input: mat = [[0,0,0],[0,1,0],[0,0,0]]
Output: [[0,0,0],[0,1,0],[0,0,0]]

Input: mat = [[0,0,0],[0,1,0],[1,1,1]]
Output: [[0,0,0],[0,1,0],[1,2,1]]
"""
from collections import deque
dirs = ((1, 0), (0, -1), (-1, 0), (0, 1))

def isValidCell(i, j, m, n):
    return i>=0 and j>=0 and i<m and j<n

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        dist = [[0 if not mat[i][j] else m+n for j in range(n)] for i in range(m)]

        q = deque()
        for i in range(m):
            for j in range(n):
                if not mat[i][j]:
                    q.append((i, j))

        while q:
            r, c = q[0]
            q.popleft()
            for d in dirs:
                nr, nc = r + d[0], c + d[1]
                if isValidCell(nr, nc, m, n) and dist[nr][nc] > dist[r][c] + 1:
                    dist[nr][nc] = dist[r][c] + 1
                    q.append((nr, nc))
        
        return dist
