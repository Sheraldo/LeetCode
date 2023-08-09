"""
https://leetcode.com/problems/minimize-the-maximum-difference-of-pairs/description/

Input: nums = [10,1,2,7,1,3], p = 2
Output: 1
Explanation: The first pair is formed from the indices 1 and 4, and the second pair is formed from the indices 2 and 5.
The maximum difference is max(|nums[1] - nums[4]|, |nums[2] - nums[5]|) = max(0, 1) = 1. Therefore, we return 1.

Input: nums = [4,2,1,2], p = 1
Output: 0
Explanation: Let the indices 1 and 3 form a pair. The difference of that pair is |2 - 2| = 0, which is the minimum we can attain.

"""
def possible(nums, max_d, p):
    cnt = 0
    i = 1
    while i < len(nums):
        if nums[i] - nums[i-1] <= max_d:
            cnt += 1
            if cnt == p: return True
            i += 2
        else:
            i += 1
    return False
class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        if p==0: return 0
        nums.sort()
        r = int(1e9)
        l = 0
        
        while l<=r:
            max_d = (l+r)//2

            if possible(nums, max_d, p):
                ans = max_d
                r = max_d - 1
            else:
                l = max_d + 1
        
        return ans
