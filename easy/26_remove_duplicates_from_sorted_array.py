"""
https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/

Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).

Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
"""
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 0
        r = 1
        while r < len(nums):
            if nums[r] == nums[l]:
                r += 1
            else:
                nums[l+1] = nums[r]
                l += 1
                r += 1
        return l+1
