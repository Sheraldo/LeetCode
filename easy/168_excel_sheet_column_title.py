"""
https://leetcode.com/problems/excel-sheet-column-title/description/

Example 1:
Input: columnNumber = 1
Output: "A"

Example 2:
Input: columnNumber = 28
Output: "AB"

Example 3:
Input: columnNumber = 701
Output: "ZY"

"""
charmap = dict(zip(range(26), string.ascii_uppercase))
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        letters = []
        while columnNumber:
            letters.append(charmap[(columnNumber-1)%26])
            columnNumber = (columnNumber-1)//26
        return ''.join(reversed(letters))
