"""
https://leetcode.com/problems/time-needed-to-inform-all-employees/description/?envType=daily-question&envId=2023-09-03

Input: n = 1, headID = 0, manager = [-1], informTime = [0]
Output: 0
Explanation: The head of the company is the only employee in the company.

Input: n = 6, headID = 2, manager = [2,2,-1,2,2,2], informTime = [0,0,1,0,0,0]
Output: 1
Explanation: The head of the company with id = 2 is the direct manager of all the employees in the company and needs 1 minute to inform them all.
The tree structure of the employees in the company is shown.
"""
class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        q = deque()
        adjList = [list() for _ in range(n)]
        for reportee, manager in enumerate(manager):
            if manager == -1:
                q.append((reportee, informTime[reportee]))
            else:
                adjList[manager].append(reportee)
        max_t = 0
        while q:
            m, t = q.popleft()
            max_t = max(t, max_t)

            for r in adjList[m]:
                q.append((r, t + informTime[r]))
        return max_t

