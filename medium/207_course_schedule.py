"""
https://leetcode.com/problems/course-schedule/description/

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take.
To take course 1 you should have finished course 0. So it is possible.

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take.
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.

"""
from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        adjList = {i:list() for i in range(numCourses)}
        for u,v in prerequisites:
            adjList[v].append(u)
            indegree[u] += 1
        
        q =deque()
        vis = [False] * numCourses
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        
        topsort = []

        while q:
            c = len(q)
            for _ in range(c):
                u = q[0]
                topsort.append(u)
                q.popleft()
                vis[u] = True
                for v in adjList[u]:
                    indegree[v] -= 1
                    if indegree[v] == 0:
                        q.append(v)
        
        return len(topsort) == numCourses
