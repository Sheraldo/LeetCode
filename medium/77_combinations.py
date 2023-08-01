ans = []
c = []
N = 0
K = 0
def make_selections(nums, i, choices_left):
    if choices_left == 0:
        ans.append(c.copy())
        return
    if i == N:
        return
    make_selections(nums,i+1,choices_left)
    c.append(nums[i])
    make_selections(nums,i+1,choices_left - 1)
    c.pop()

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        global N,K
        ans.clear()
        c.clear()
        N = n
        K = k
        choices_left = k
        nums = [i for i in range(1,n+1)]
        make_selections(nums, 0, choices_left)
        return ans
