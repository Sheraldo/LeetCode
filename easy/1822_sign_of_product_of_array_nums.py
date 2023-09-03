"""
https://leetcode.com/problems/sign-of-the-product-of-an-array/description/?envType=daily-question&envId=2023-09-03

Input: nums = [-1,-2,-3,-4,3,2,1]
Output: 1
Explanation: The product of all values in the array is 144, and signFunc(144)

Input: nums = [1,5,0,2,-3]
Output: 0
Explanation: The product of all values in the array is 0, and signFunc(0) = 0

Input: nums = [-1,1,-1,1,-1]
Output: -1
Explanation: The product of all values in the array is -1, and signFunc(-1) = -1

"""
class Solution:
    def arraySign(self, nums: List[int]) -> int:
        neg = 0
        n = len(nums)
        for n in nums:
            if n < 0:
                neg += 1
            elif n == 0:
                return 0
        return 1 if neg % 2 == 0 else -1

