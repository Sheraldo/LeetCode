"""
https://leetcode.com/problems/group-the-people-given-the-group-size-they-belong-to/description/?envType=daily-question&envId=2023-09-11

Input: groupSizes = [3,3,3,3,3,1,3]
Output: [[5],[0,1,2],[3,4,6]]
Explanation:
The first group is [5]. The size is 1, and groupSizes[5] = 1.
The second group is [0,1,2]. The size is 3, and groupSizes[0] = groupSizes[1] = groupSizes[2] = 3.
The third group is [3,4,6]. The size is 3, and groupSizes[3] = groupSizes[4] = groupSizes[6] = 3.
Other possible solutions are [[2,1,6],[5],[0,4,3]] and [[5],[0,6,2],[4,3,1]].

Input: groupSizes = [2,1,3,3,3,2]
Output: [[1],[0,5],[2,3,4]]
"""
class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        d = {}
        for gs in groupSizes:
            d[gs] = list()
        
        n = len(groupSizes)

        for i, gs in enumerate(groupSizes):
            if d[gs]:
                if len(d[gs][-1]) == gs:
                    d[gs].append([i])
                else:
                    d[gs][-1].append(i)
            else:
                d[gs].append([i])
        
        ret = []
        for k, l, in d.items():
            ret.extend(l)
        return ret

