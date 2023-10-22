"""
https://leetcode.com/problems/maximum-score-of-a-good-subarray/?envType=daily-question&envId=2023-10-22

Example 1:

Input: nums = [1,4,3,7,4,5], k = 3
Output: 15
Explanation: The optimal subarray is (1, 5) with a score of min(4,3,7,4,5) * (5-1+1) = 3 * 5 = 15.

Example 2:

Input: nums = [5,5,4,5,4,1,1,1], k = 0
Output: 20
Explanation: The optimal subarray is (0, 4) with a score of min(5,5,4,5,4) * (4-0+1) = 4 * 5 = 20.



Constraints:

    1 <= nums.length <= 105
    1 <= nums[i] <= 2 * 104
    0 <= k < nums.length

"""
class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        l = r = k
        ans = nums[k]
        cur_min = nums[k]

        while l > 0 or r < len(nums) - 1:
            left = nums[l-1] if l>0 else 0
            right = nums[r+1] if r+1<len(nums) else 0

            if left > right:
                l -= 1
                cur_min = min(left, cur_min)
            else:
                r += 1
                cur_min = min(right, cur_min)

            ans = max(ans, cur_min * (r-l+1))
        
        return ans

