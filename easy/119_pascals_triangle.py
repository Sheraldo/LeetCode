"""
https://leetcode.com/problems/pascals-triangle-ii/?envType=daily-question&envId=2023-10-16

Example 1:

Input: rowIndex = 3
Output: [1,3,3,1]

Example 2:

Input: rowIndex = 0
Output: [1]

Example 3:

Input: rowIndex = 1
Output: [1,1]



Constraints:

    0 <= rowIndex <= 33

"""
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        ans = [1]

        for i in range(rowIndex):
            next_row = [0] * (len(ans) + 1)
            for j in range(len(ans)):
                next_row[j] += ans[j]
                next_row[j+1] += ans[j]
            ans = next_row
        
        return ans

