"""
https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/

Constraints:

    0 <= digits.length <= 4
    digits[i] is a digit in the range ['2', '9'].


Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Input: digits = ""
Output: []

Input: digits = "2"
Output: ["a","b","c"]
"""
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {
                    '2':'abc',
                    '3':'def',
                    '4':'ghi',
                    '5':'jkl',
                    '6':'mno',
                    '7':'pqrs',
                    '8':'tuv',
                    '9':'wxyz'
        }
        curr_s = []
        ans = []
        n=len(digits)

        def genPerm(i):
            if i== n:
                if curr_s: ans.append("".join(curr_s))
                return
            else:
                for c in mapping[digits[i]]:
                    curr_s.append(c)
                    genPerm(i+1)
                    curr_s.pop()
        genPerm(0)
        return ans
