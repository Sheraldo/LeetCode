"""
https://leetcode.com/problems/reorganize-string/description/

Input: s = "aab"
Output: "aba"

Input: s = "aaab"
Output: ""
"""
class Solution:
    def reorganizeString(self, s: str) -> str:
        cnt = Counter(s)
        maxHeap = [(-value, key) for key, value in cnt.items()]
        heapq.heapify(maxHeap)

        prev = None
        ans = ""
        while maxHeap or prev:
            # if we have a prev and exhausted next choice we will have to repeat
            if prev and not maxHeap:
                return ""

            cnt,c = heapq.heappop(maxHeap)
            ans += c
            cnt += 1 # since count stored is negative

            if prev:
                heapq.heappush(maxHeap, prev)
                prev = None

            if cnt != 0:
                prev = (cnt, c)
        return ans

