"""
https://leetcode.com/problems/peak-index-in-a-mountain-array/description/

Input: arr = [0,1,0]
Output: 1

Input: arr = [0,2,1,0]
Output: 1

Input: arr = [0,10,5,2]
Output: 1
"""
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        n = len(arr)
        l, r = 0, n-1

        while l <= r:
            m = (l+r)//2

            if arr[m] > arr[m-1] and arr[m] > arr[m+1]:
                return m
            elif arr[m-1] < arr[m] and arr[m] < arr[m+1]:
                l = m
            else:
                r = m
