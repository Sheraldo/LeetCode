"""
Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.

Input: nums = [2,3,0,1,4]
Output: 2

"""
class Solution:
    def jump(self, nums: List[int]) -> int:
        ans = 0
        l = r = 0
        n = len(nums)
        while r < n-1:
            reach = 0
            for i in range(l,r+1):
                reach = max(reach,i + nums[i])
            ans += 1
            l = r+1
            r = reach
        return ans
