"""
https://leetcode.com/problems/search-in-rotated-sorted-array/description/

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1

Input: nums = [1], target = 0
Output: -1
"""
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        h = len(nums) - 1
        m = 0
        ans = -1

        while l<=h:
            m = (l+h)//2
            if nums[m]==target:
                ans = m
                break

            if nums[l] <= nums[m]:
                if (target > nums[m]) or (target < nums[l]):
                    l = m + 1
                else: h = m - 1
            else:
                if (target < nums[m]) or (target > nums[h]):
                    h = m - 1
                else: l = m + 1
        
        return ans
