"""
https://leetcode.com/problems/sort-array-by-parity/?envType=daily-question&envId=2023-09-28

Example 1:

Input: nums = [3,1,2,4]
Output: [2,4,3,1]
Explanation: The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.

Example 2:

Input: nums = [0]
Output: [0]



Constraints:

    1 <= nums.length <= 5000
    0 <= nums[i] <= 5000

"""
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        p1, p2 = 0, 0
        while p2 < len(nums):
            if nums[p2] % 2 == 0:
                nums[p1], nums[p2] = nums[p2], nums[p1]
                p1 += 1
            p2 += 1
        return nums

