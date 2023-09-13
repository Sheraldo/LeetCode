"""
https://leetcode.com/problems/candy/description/?envType=daily-question&envId=2023-09-13

Input: ratings = [1,0,2]
Output: 5
Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.

Input: ratings = [1,2,2]
Output: 4
Explanation: You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
The third child gets 1 candy because it satisfies the above two conditions.
"""
class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        left_satisfied = [1] * n
        right_satisfied = [1] * n
        for i in range(1, n):
            if ratings[i] > ratings[i-1]:
                left_satisfied[i] = left_satisfied[i-1] + 1

        for i in range(n-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                right_satisfied[i] = right_satisfied[i+1] + 1
        ans = 0
        for i in range(n):
            ans += max(left_satisfied[i], right_satisfied[i])
        return ans

