"""
https://leetcode.com/problems/average-salary-excluding-the-minimum-and-maximum-salary/description/?envType=daily-question&envId=2023-09-12

Input: salary = [4000,3000,1000,2000]
Output: 2500.00000
Explanation: Minimum salary and maximum salary are 1000 and 4000 respectively.
Average salary excluding minimum and maximum salary is (2000+3000) / 2 = 2500

Input: salary = [1000,2000,3000]
Output: 2000.00000
Explanation: Minimum salary and maximum salary are 1000 and 3000 respectively.
Average salary excluding minimum and maximum salary is (2000) / 1 = 2000

Constraints:

    3 <= salary.length <= 100
    1000 <= salary[i] <= 106
    All the integers of salary are unique.

"""
class Solution:
    def average(self, salary: List[int]) -> float:
        n = len(salary)
        heapq.heapify(salary)
        heappop(salary)
        s = 0
        for i in range(n-2):
            s += heappop(salary)
        return s/(n-2)
