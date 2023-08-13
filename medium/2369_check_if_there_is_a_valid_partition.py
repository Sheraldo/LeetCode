"""
https://leetcode.com/problems/check-if-there-is-a-valid-partition-for-the-array/description/

Input: nums = [4,4,4,5,6]
Output: true
Explanation: The array can be partitioned into the subarrays [4,4] and [4,5,6].
This partition is valid, so we return true.

Input: nums = [1,1,1,2]
Output: false
Explanation: There is no valid partition for this array.
"""
class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [None]*(n+1)
        dp[n] = True

        def validP(i, nums):
            if dp[i] is not None: return dp[i]
            ret = False
            if i+1<len(nums) and nums[i]==nums[i+1]:
                ret |= validP(i+2,nums)
            if i+1<len(nums) and i+2<len(nums) and nums[i] == nums[i+1] == nums[i+2]:
                ret |= validP(i+3,nums)
            if (i+1<len(nums) and i+2<len(nums) and
                nums[i] == nums[i+1]-1 and nums[i+1] == nums[i+2]-1):
                ret |= validP(i+3,nums)
            dp[i] = ret
            return dp[i]
        return validP(0, nums)

