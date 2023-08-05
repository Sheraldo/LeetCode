"""
https://leetcode.com/problems/longest-consecutive-sequence/description/

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
"""
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        longest = 0

        for n in nums:
            if n-1 not in s:
                l = 0
                while n+l in s:
                    l+=1
                longest = max(longest,l)
        return longest
                
