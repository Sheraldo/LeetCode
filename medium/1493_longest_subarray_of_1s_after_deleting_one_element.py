"""
https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/?envType=daily-question&envId=2023-09-30

Example 1:

Input: nums = [1,1,0,1]
Output: 3
Explanation: After deleting the number in position 2, [1,1,1] contains 3 numbers with value of 1's.

Example 2:

Input: nums = [0,1,1,1,0,1,1,0,1]
Output: 5
Explanation: After deleting the number in position 4, [0,1,1,1,1,1,0,1] longest subarray with value of 1's is [1,1,1,1,1].

Example 3:

Input: nums = [1,1,1]
Output: 2
Explanation: You must delete one element.



Constraints:

    1 <= nums.length <= 105
    nums[i] is either 0 or 1.

"""
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        i = 0
        n = len(nums)
        compressed = []

        while i<n:
            if nums[i] == 0:
                compressed.append(0)
            else:
                j = i
                cnt = 0
                while j<n and nums[j]==1:
                    cnt += 1
                    j += 1
                i = j
                compressed.append(cnt)
                if j<n:
                    compressed.append(0)
            i += 1

        if len(compressed) == 1:
            if compressed[0] != 0:
                return compressed[0] - 1
            else:
                return 0
        else:
            ans = 0
            for i, cnt in enumerate(compressed):
                if cnt == 0:
                    pre = 0 if i==0 else compressed[i-1]
                    post = 0 if i==len(compressed)-1 else compressed[i+1]
                    ans = max(ans, pre+post)
            return ans

