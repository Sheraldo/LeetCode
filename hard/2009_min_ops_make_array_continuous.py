"""
https://leetcode.com/problems/minimum-number-of-operations-to-make-array-continuous/?envType=daily-question&envId=2023-10-10

Example 1:

Input: nums = [4,2,5,3]
Output: 0
Explanation: nums is already continuous.

Example 2:

Input: nums = [1,2,3,5,6]
Output: 1
Explanation: One possible solution is to change the last element to 4.
The resulting array is [1,2,3,5,4], which is continuous.

Example 3:

Input: nums = [1,10,100,1000]
Output: 3
Explanation: One possible solution is to:
- Change the second element to 2.
- Change the third element to 3.
- Change the fourth element to 4.
The resulting array is [1,2,3,4], which is continuous.



Constraints:

    1 <= nums.length <= 105
    1 <= nums[i] <= 109

"""
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        duplicates = [0] * n
        values = set()
        dcount = 0

        for i in range(n):
            if nums[i] in values:
                dcount += 1
            else:
                values.add(nums[i])
            duplicates[i] = dcount
        
        ans = n-1
        l = 0
        for i in range(n):
            while l<=i and nums[i] - nums[l] > n - 1:
                l += 1
            satisfying = i - l + 1
            dupl = duplicates[i]
            if l > 0:
                dupl -= duplicates[l - 1]
            swap_count = dupl + n - satisfying
            ans = min(ans, swap_count)
        
        return ans

