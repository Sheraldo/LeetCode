"""
https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/description/

Input: nums = [1,1,1,2,2,3]
Output: 5, nums = [1,1,2,2,3,_]
Explanation: Your function should return k = 5, with the first five elements of nums being 1, 1, 2, 2 and 3 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).

Input: nums = [0,0,1,1,1,1,2,3,3]
Output: 7, nums = [0,0,1,1,2,3,3,_,_]
Explanation: Your function should return k = 7, with the first seven elements of nums being 0, 0, 1, 1, 2, 3 and 3 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
"""
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 0
        r = 0

        while r < len(nums):
            count = 1
            while r+1<len(nums) and nums[r] == nums[r+1]:
                count += 1
                r += 1
            for i in range(min(2, count)):
                nums[l] = nums[r]
                l += 1
            r += 1
        return l

