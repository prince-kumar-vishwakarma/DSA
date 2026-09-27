# 225. Implement Stack using Queues

from collections import deque
class MyStack:

    def __init__(self):
        self.q = deque()
        self.ele = 0

    def push(self, x: int) -> None:
        self.q.append(x)
        self.ele += 1
        

    def pop(self) -> int:
        self.ele -= 1
        for _ in range(self.ele):
            self.q.append(self.q.popleft())
        return self.q.popleft()


    def top(self) -> int:
        for _ in range(self.ele-1):
            self.q.append(self.q.popleft())
        x = self.q.popleft()
        self.q.append(x)

        return x

        

    def empty(self) -> bool:
        return self.ele == 0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()