"""
https://leetcode.com/problems/put-marbles-in-bags/description/?envType=daily-question&envId=2023-09-05

Input: weights = [1,3,5,1], k = 2
Output: 4
Explanation:
The distribution [1],[3,5,1] results in the minimal score of (1+1) + (3+1) = 6.
The distribution [1,3],[5,1], results in the maximal score of (1+3) + (5+1) = 10.
Thus, we return their difference 10 - 6 = 4.

Input: weights = [1, 3], k = 2
Output: 0
Explanation: The only distribution possible is [1],[3].
Since both the maximal and minimal score are the same, we return 0.
"""
class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        if k==1 or k == len(weights): return 0

        as_bag_end_cost_mn = [weights[i] + weights[i+1] 
                                for i in range(len(weights) - 1)]
        as_bag_end_cost_mx = [-x for x in as_bag_end_cost_mn]
        # choose k - 1 bag ends for max and min
        heapq.heapify(as_bag_end_cost_mx)
        heapq.heapify(as_bag_end_cost_mn)

        count = k - 1
        min_cost = 0
        max_cost = 0
        while count:
            min_cost += heapq.heappop(as_bag_end_cost_mn)
            max_cost += -heapq.heappop(as_bag_end_cost_mx)
            count -= 1
        
        return max_cost - min_cost
