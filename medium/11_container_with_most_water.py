"""
https://leetcode.com/problems/container-with-most-water/description/

Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

Input: height = [1,1]
Output: 1
"""
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        max_water = -1
        while l<r:
            max_water = max(max_water, min(height[r],height[l]) * (r-l))
            if height[l] <= height[r]: l += 1
            else: r -= 1
        return max_water
