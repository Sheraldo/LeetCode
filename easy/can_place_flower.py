"""
https://leetcode.com/problems/can-place-flowers/description/

Input: flowerbed = [1,0,0,0,1], n = 1
Output: true

Input: flowerbed = [1,0,0,0,1], n = 2
Output: false
"""
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        f = len(flowerbed)
        flowerbed.insert(0,0)
        flowerbed.append(0)
        pot = 0
        if n == 0: return True

        for i in range(1,f+1):
            if flowerbed[i-1]==0 and flowerbed[i]==0 and flowerbed[i+1]==0:
                pot += 1
                flowerbed[i] = 1
                if pot == n: return True
        return False

