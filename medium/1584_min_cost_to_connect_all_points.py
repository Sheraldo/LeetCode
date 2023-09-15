"""
https://leetcode.com/problems/min-cost-to-connect-all-points/description/?envType=daily-question&envId=2023-09-15

Input: points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
Output: 20
We can connect the points as shown above to get the minimum cost of 20.
Notice that there is a unique path between every pair of points.

Input: points = [[3,12],[-2,5],[-4,1]]
Output: 18
"""
def manhatten_dist(i, j, points):
    return abs(points[i][0]-points[j][0]) + abs(points[i][1]-points[j][1])

def find_parent(i, parent):
    if parent[i] != i:
        parent[i] = find_parent(parent[i], parent)
    return parent[i]

def union_points(i, j, parent, rank):
    pi = find_parent(i, parent)
    pj = find_parent(j, parent)
    if pi == pj:
        return False
    else:
        if rank[pi] >= rank[pj]:
            parent[pj] = pi
            rank[pi] += rank[pj]
        else:
            parent[pi] = pj
            rank[pj] += rank[pi]
        return True

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        parent = [i for i in range(n)]
        rank = [1 for _ in range(n)]
        edges = list()

        for i in range(n):
            for j in range(i + 1, n):
                d = manhatten_dist(i, j, points)
                heappush(edges, (d, i, j))
        
        mst = 0
        mst_edges = 0
        
        while edges:
            d, s, e = heappop(edges)
            if union_points(s, e, parent, rank):
                mst += d
                mst_edges += 1
                if mst_edges == n-1:
                    break
        
        return mst

