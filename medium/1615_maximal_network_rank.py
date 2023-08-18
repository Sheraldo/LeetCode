"""
https://leetcode.com/problems/maximal-network-rank/description/

Input: n = 4, roads = [[0,1],[0,3],[1,2],[1,3]]
Output: 4
Explanation: The network rank of cities 0 and 1 is 4 as there are 4 roads that are connected to either 0 or 1. The road between 0 and 1 is only counted once.

Input: n = 5, roads = [[0,1],[0,3],[1,2],[1,3],[2,3],[2,4]]
Output: 5
Explanation: There are 5 roads that are connected to cities 1 or 2.


Input: n = 8, roads = [[0,1],[1,2],[2,3],[2,4],[5,6],[5,7]]
Output: 5
Explanation: The network rank of 2 and 5 is 5. Notice that all the cities do not have to be connected.
"""
class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        adjList = [set() for i in range(n)]
        degree = [0] * n
        vis = [False] * n

        for u, v in roads:
            adjList[u].add(v)
            adjList[v].add(u)
            degree[u] += 1
            degree[v] += 1
        
        max_netw_val = 0
        
        for u in range(n):
            for v in range(n):
                if v == u: continue
                c_val = degree[u] + degree[v]
                if v in adjList[u]: c_val -= 1
                max_netw_val = max(c_val, max_netw_val)
        return max_netw_val
