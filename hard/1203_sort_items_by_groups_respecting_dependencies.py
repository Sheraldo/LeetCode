"""
https://leetcode.com/problems/sort-items-by-groups-respecting-dependencies/

Input: n = 8, m = 2, group = [-1,-1,1,0,0,1,0,-1], beforeItems = [[],[6],[5],[6],[3,6],[],[],[]]
Output: [6,3,4,1,5,2,0,7]

Input: n = 8, m = 2, group = [-1,-1,1,0,0,1,0,-1], beforeItems = [[],[6],[5],[6],[3],[],[4],[]]
Output: []
Explanation: This is the same as example 1 except that 4 needs to be before 6 in the sorted list.
"""
class Solution:

    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        def topsort(nodes, graph, indegree):
            q = collections.deque(node for node in nodes if node not in indegree)
            ans = []
            while q:
                cn = q.popleft()
                ans.append(cn)

                for nbr in graph[cn]:
                    indegree[nbr] -= 1
                    if indegree[nbr] == 0:
                        q.append(nbr)
            return ans
        
        grpitems = defaultdict(list)
        grpid = m

        for i in range(n):
            if group[i] == -1:
                group[i] = grpid
                grpid += 1
            
            
            grpitems[group[i]].append(i)
        
        itmgraph = defaultdict(list)
        itmindegree = defaultdict(int)

        for v, u_list in enumerate(beforeItems):
            for u in u_list:
                if group[u] == group[v]:
                    itmgraph[u].append(v)
                    itmindegree[v] += 1

        sorted_grpitems = {}

        for grpid in grpitems:
            sorteditems = topsort(grpitems[grpid], itmgraph, itmindegree)
            if len(sorteditems) != len(grpitems[grpid]):
                return []
            sorted_grpitems[grpid]=sorteditems
        
        groupgraph = defaultdict(list)
        groupindegree = defaultdict(int)

        for v, u_list in enumerate(beforeItems):
            for u in u_list:
                if group[u] != group[v]:
                    groupgraph[group[u]].append(group[v])
                    groupindegree[group[v]] += 1
        
        groups = set(group)
        sortedgroups = topsort(groups, groupgraph, groupindegree)
        if len(sortedgroups) != len(groups):
            return []

        ans = []

        for grpid in sortedgroups:
            ans.extend(sorted_grpitems[grpid])
        
        return ans

