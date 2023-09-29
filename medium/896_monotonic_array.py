"""
https://leetcode.com/problems/monotonic-array/?envType=daily-question&envId=2023-09-29

Example 1:

Input: nums = [1,2,2,3]
Output: true

Example 2:

Input: nums = [6,5,4,4]
Output: true

Example 3:

Input: nums = [1,3,2]
Output: false



Constraints:

    1 <= nums.length <= 105
    -105 <= nums[i] <= 105

"""
class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        i = 0
        is_increasing, is_decreasing = True, True
        while (i + 1)<len(nums) and (is_increasing or is_decreasing):
            if nums[i] < nums[i+1]:
                is_decreasing = False
            if nums[i] > nums[i+1]:
                is_increasing = False
            i += 1
        return (is_increasing or is_decreasing)

