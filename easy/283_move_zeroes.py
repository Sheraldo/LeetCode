"""
https://leetcode.com/problems/move-zeroes/description/

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

Input: nums = [0]
Output: [0]
"""
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        p1 = n-1
        zero_count = 0
        while p1 >= 0:
            if nums[p1] == 0:
                zero_count += 1
                nums.pop(p1)
            p1 -= 1
        nums.extend([0]*zero_count)
