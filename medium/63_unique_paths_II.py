"""
https://leetcode.com/problems/unique-paths-ii/description/

Input: obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
Output: 2
Explanation: There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right

Input: obstacleGrid = [[0,1],[0,0]]
Output: 1
"""
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0 for i in range(n)] for j in range(m)]
        if obstacleGrid[m-1][n-1] == 1 or obstacleGrid[0][0] == 1: return 0

        for j in range(n):
            if obstacleGrid[0][j] == 0: dp[0][j] = 1
            else: break
        
        for i in range(m):
            if obstacleGrid[i][0] == 0: dp[i][0] = 1
            else: break
        
        for i in range(1,m):
            for j in range(1,n):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        return dp[m-1][n-1]

