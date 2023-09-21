"""
Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.



Constraints:

    nums1.length == m
    nums2.length == n
    0 <= m <= 1000
    0 <= n <= 1000
    1 <= m + n <= 2000
    -106 <= nums1[i], nums2[i] <= 106

"""
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l1, l2 = nums1, nums2
        if len(l2) < len(l1):
            l1, l2 = l2, l1
        # l1 is the smaller array

        total = len(nums1) + len(nums2)
        half = total // 2

        l, r = 0, len(l1) - 1

        while True:
            i = (l+r)>>1
            j = half - i - 2

            l1_left = l1[i] if i >= 0 else float('-inf')
            l1_right = l1[i+1] if (i+1)<len(l1) else float('inf')
            l2_left = l2[j] if j >= 0 else float('-inf')
            l2_right = l2[j+1] if (j+1)<len(l2) else float('inf')

            if l1_left <= l2_right and l2_left <= l1_right:
                if total & 1:
                    return min(l1_right, l2_right)
                else:
                    return (max(l1_left, l2_left) + min(l1_right, l2_right)) / 2
            elif l1_left > l2_right:
                r = i - 1
            else:
                l = i + 1

