"""
https://leetcode.com/problems/shortest-path-visiting-all-nodes/description/?envType=daily-question&envId=2023-09-17


Input: graph = [[1,2,3],[0],[0],[0]]
Output: 4
Explanation: One possible path is [1,0,2,0,3]

Input: graph = [[1],[0,2,4],[1,3,4],[2],[1,2]]
Output: 4
Explanation: One possible path is [0,1,4,2,3]
"""
from collections import deque
class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        if len(graph) == 1: return 0

        final_state = (1<<len(graph)) - 1
        q = deque()

        for i in range(len(graph)):
            q.append((i, 1<<i))

        vis = [[False]*(final_state + 1) for _ in range(len(graph))]

        shortest_path = 0

        while q:
            l = len(q)
            shortest_path += 1
            for _ in range(l):
                u, bitstate = q.popleft()
                for v in graph[u]:
                    nbitstate = bitstate | (1<<v)
                    if vis[v][nbitstate]: continue
                    vis[v][nbitstate] = True
                    if nbitstate == final_state:
                        return shortest_path
                    q.append((v, nbitstate))

