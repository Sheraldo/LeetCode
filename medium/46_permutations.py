"""
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Input: nums = [0,1]
Output: [[0,1],[1,0]]

Input: nums = [1]
Output: [[1]]

"""
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []
        def genPerm(nums, i):
            if i==n:
                ans.append(nums[:])
                return
            genPerm(nums,i+1)
            for j in range(i+1,n):
                nums[i], nums[j] = nums[j], nums[i]
                genPerm(nums,i+1)
                nums[i], nums[j] = nums[j], nums[i]
        genPerm(nums, 0)
        return ans
