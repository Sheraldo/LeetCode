"""
https://leetcode.com/problems/asteroid-collision/description/

Input: asteroids = [5,10,-5]
Output: [5,10]
Explanation: The 10 and -5 collide resulting in 10. The 5 and 10 never collide.

Input: asteroids = [8,-8]
Output: []
Explanation: The 8 and -8 collide exploding each other.

Input: asteroids = [10,2,-5]
Output: [10]
Explanation: The 2 and -5 collide resulting in -5. The 10 and -5 collide resulting in 10.
"""
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        output = []

        for v in asteroids:
            if v >= 0: output.append(v)
            else:
                while output and output[-1] >=0 and output[-1] < abs(v):
                    output.pop()
                if output and output[-1] >=0 and output[-1] == abs(v):
                    output.pop()
                    continue
                if not output or output[-1] < 0: output.append(v)
        return output
