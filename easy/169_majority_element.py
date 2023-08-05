"""
https://leetcode.com/problems/majority-element/description/

Input: nums = [3,2,3]
Output: 3

Input: nums = [2,2,1,1,1,2,2]
Output: 2
"""
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # obvious soln is hashmap but to answer follow up
        # boyer moore algorithm

        res, count = 0, 0

        for n in nums:
            if count == 0: res = n

            count += 1 if n == res else -1
        return res
