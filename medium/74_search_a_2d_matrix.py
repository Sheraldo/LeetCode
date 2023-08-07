"""
https://leetcode.com/problems/search-a-2d-matrix/description/

Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true

Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false
"""
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        i=0
        j=cols-1

        while i<rows and j>=0:
            # print(matrix[i][j])
            if matrix[i][j]==target:
                return True
            elif matrix[i][j] > target:
                j -= 1
            else:
                i += 1
        return False
