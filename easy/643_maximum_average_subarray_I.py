"""
https://leetcode.com/problems/maximum-average-subarray-i/description/

Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000
Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75

Input: nums = [5], k = 1
Output: 5.00000

"""
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        s = sum(nums[:k])
        l,r = 0,k-1
        max_avg = s/k
        r+=1
        while r<len(nums):
            s += nums[r]
            s -= nums[l]
            l += 1
            r += 1
            max_avg = max(max_avg, s/k)
        return max_avg
