"""
https://leetcode.com/problems/minimum-replacements-to-sort-the-array/description/

Input: nums = [3,9,3]
Output: 2
Explanation: Here are the steps to sort the array in non-decreasing order:
- From [3,9,3], replace the 9 with 3 and 6 so the array becomes [3,3,6,3]
- From [3,3,6,3], replace the 6 with 3 and 3 so the array becomes [3,3,3,3,3]
There are 2 steps to sort the array in non-decreasing order. Therefore, we return 2.

Input: nums = [1,2,3,4,5]
Output: 0
Explanation: The array is already in non-decreasing order. Therefore, we return 0.
"""
class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        n = len(nums)
        count = 0

        max_val = nums[-1]

        for i in range(n-2, -1, -1):
            if nums[i] > max_val:
                c = math.ceil(nums[i]/max_val)
                count += c - 1
                max_val = nums[i] // c
            else:
                max_val = nums[i]
        
        return count

