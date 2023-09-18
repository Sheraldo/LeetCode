"""
https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/?envType=daily-question&envId=2023-09-18

Example 1:

Input: mat =
[[1,1,0,0,0],
 [1,1,1,1,0],
 [1,0,0,0,0],
 [1,1,0,0,0],
 [1,1,1,1,1]],
k = 3
Output: [2,0,3]
Explanation:
The number of soldiers in each row is:
- Row 0: 2
- Row 1: 4
- Row 2: 1
- Row 3: 2
- Row 4: 5
The rows ordered from weakest to strongest are [2,0,3,1,4].

Example 2:

Input: mat =
[[1,0,0,0],
 [1,1,1,1],
 [1,0,0,0],
 [1,0,0,0]],
k = 2
Output: [0,2]
Explanation:
The number of soldiers in each row is:
- Row 0: 1
- Row 1: 4
- Row 2: 1
- Row 3: 1
The rows ordered from weakest to strongest are [0,2,3,1].



Constraints:

    m == mat.length
    n == mat[i].length
    2 <= n, m <= 100
    1 <= k <= m
    matrix[i][j] is either 0 or 1.

"""
def get_soldier_count(mat, i):
    l, r = 0, len(mat[i]) - 1
    if mat[i][r] ==1:
        return len(mat[i])
    elif mat[i][l] == 0:
        return 0
    ans = l
    while l<=r:
        m = (l+r)>>1
        if mat[i][m] == 1:
            ans = m
            l = m + 1
        else:
            r = m - 1
    return ans + 1
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        data = [(get_soldier_count(mat, i), i) for i in range(len(mat))]
        heapq.heapify(data)
        print(data)
        ans = [None] * k
        for i in range(k):
            ans[i] = heappop(data)[1]
        return ans

