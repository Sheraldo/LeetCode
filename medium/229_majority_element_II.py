"""
https://leetcode.com/problems/majority-element-ii/?envType=daily-question&envId=2023-10-05

Example 1:

Input: nums = [3,2,3]
Output: [3]

Example 2:

Input: nums = [1]
Output: [1]

Example 3:

Input: nums = [1,2]
Output: [1,2]



Constraints:

    1 <= nums.length <= 5 * 104
    -109 <= nums[i] <= 109

Follow up: Could you solve the problem in linear time and in O(1) space?
"""
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = defaultdict(int)

        for n in nums:
            count[n] += 1
            if len(count) <= 2:
                continue
            new_count = defaultdict(int)
            for n, cnt in count.items():
                if cnt > 1:
                    new_count[n] = cnt - 1
            count = new_count
        
        res = [n for n in count if nums.count(n) > len(nums)//3]
        return res

