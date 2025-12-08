from collections import deque


# class MyQueue:
#
#     def __init__(self):
#         self.q = deque()
#
#     def push(self, x: int) -> None:
#         self.q.append(x)
#
#     def pop(self) -> int:
#         return self.q.popleft()
#
#     def peek(self) -> int:
#         return self.q[0]
#
#     def empty(self) -> bool:
#         return len(self.q) == 0


class MyQueue:

    def __init__(self):
        self.q1 = []
        self.q2 = []

    def push(self, x: int) -> None:
        self.q1.append(x)

    def pop(self) -> int:
        self.peek()
        return self.q2.pop()

    def peek(self) -> int:
        if not self.q2:
            while self.q1:
                self.q2.append(self.q1.pop())

        return self.q2[-1]

    def empty(self) -> bool:
        return len(self.q1) == 0 and len(self.q2) == 0