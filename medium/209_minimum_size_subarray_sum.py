"""
https://leetcode.com/problems/minimum-size-subarray-sum/description/

Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.

Input: target = 4, nums = [1,4,4]
Output: 1

Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0
"""
import itertools
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        """
        subarray len ranges from 1, len(nums)
        """
        n = len(nums)
        low = 1
        high = n - 1
        pfsum = list(itertools.accumulate(nums))
        def sum_possible(c_len):
            l = 0
            r = c_len-1
            s = pfsum[r] - (pfsum[l-1] if l-1 >= 0 else 0)
            max_s = s
            r += 1
            while r < n:
                s = s + nums[r] - nums[l]
                max_s = max(max_s,s)
                r += 1
                l += 1
            return max_s >= target
            
        ans = 0
        if pfsum[n-1] >= target: ans = n
        while low <= high:
            c_len = (low + high)//2
            if sum_possible(c_len):
                ans = c_len
                high = c_len - 1
            else:
                low = c_len + 1
        return ans
