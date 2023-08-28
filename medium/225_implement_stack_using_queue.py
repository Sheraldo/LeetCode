"""
https://leetcode.com/problems/implement-stack-using-queues/description/

Input
["MyStack", "push", "push", "top", "pop", "empty"]
[[], [1], [2], [], [], []]
Output
[null, null, null, 2, 2, false]

Follow-up: Can you implement the stack using only one queue?
"""
class MyStack:

    def __init__(self):
        self.q = deque()
        self.count = 0

    def push(self, x: int) -> None:
        self.q.append(x)
        self.count += 1
        

    def pop(self) -> int:
        c = self.count - 1
        while c:
            x = self.q.popleft()
            self.q.append(x)
            c -= 1
        self.count -= 1
        return self.q.popleft()
        

    def top(self) -> int:
        return self.q[-1]
        

    def empty(self) -> bool:
        return self.count == 0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
