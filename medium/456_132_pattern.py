"""
https://leetcode.com/problems/132-pattern/?envType=daily-question&envId=2023-09-30

Example 1:

Input: nums = [1,2,3,4]
Output: false
Explanation: There is no 132 pattern in the sequence.

Example 2:

Input: nums = [3,1,4,2]
Output: true
Explanation: There is a 132 pattern in the sequence: [1, 4, 2].

Example 3:

Input: nums = [-1,3,2,0]
Output: true
Explanation: There are three 132 patterns in the sequence: [-1, 3, 2], [-1, 3, 0] and [-1, 2, 0].
"""
class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = [] # [max_left, min_before]
        min_so_far = nums[0]
        for x in nums[1:]:
            while stack and x >= stack[-1][0]:
                stack.pop()
            if stack and x < stack[-1][0] and x > stack[-1][1]:
                return True
            stack.append((x, min_so_far))
            min_so_far = min(min_so_far, x)
        return False

