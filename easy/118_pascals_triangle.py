"""
https://leetcode.com/problems/pascals-triangle/description/?envType=daily-question&envId=2023-09-08

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

Input: numRows = 1
Output: [[1]]
"""
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = [[1]]
        for i in range(2, numRows + 1):
            l = [1] * i
            for j in range(1, i - 1):
                l[j] = ans[-1][j - 1] + ans[-1][j]
            ans.append(l)
        return ans

