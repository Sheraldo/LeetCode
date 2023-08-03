"""
https://leetcode.com/problems/merge-sorted-array/description/

Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.

Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]
Explanation: The arrays we are merging are [1] and [].
The result of the merge is [1].

Input: nums1 = [0], m = 0, nums2 = [1], n = 1
Output: [1]
Explanation: The arrays we are merging are [] and [1].
The result of the merge is [1].
Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.

"""
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n == 0:
            return None
        if m == 0:
            for i, x in enumerate(nums2):
                nums1[i] = x
            return None
        p1 = m-1
        p2 = n-1
        fi = len(nums1) - 1

        while p1 >= 0 and p2 >=0:
            if nums2[p2] >= nums1[p1]:
                nums1[fi] = nums2[p2]
                p2 -= 1
            else:
                nums1[fi] = nums1[p1]
                p1 -= 1
            fi -= 1
        while p1 >= 0:
            nums1[fi] = nums1[p1]
            p1 -= 1
            fi -= 1
        while p2 >= 0:
            nums1[fi] = nums2[p2]
            p2 -= 1
            fi -= 1
