"""
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

Input: nums = [], target = 0
Output: [-1,-1]
"""
class Solution:
    def get_first_occurrence(self, nums, s, e, target):
        ans = -1
        while s <= e:
            mid = (s+e)//2
            if nums[mid] == target:
                ans = mid
                e = mid - 1
            elif nums[mid] < target:
                s = mid + 1
            else:
                e = mid - 1
        return ans
    def get_last_occurrence(self, nums, s, e, target):
        ans = -1
        while s <= e:
            mid = (s+e)//2
            if nums[mid] == target:
                ans = mid
                s = mid + 1
            elif nums[mid] < target:
                s = mid + 1
            else:
                e = mid - 1
        return ans
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        l = self.get_first_occurrence(nums, 0, n-1, target)
        r = self.get_last_occurrence(nums, 0, n-1, target)
        return (l,r)
