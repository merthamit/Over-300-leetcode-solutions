from collections import deque
import collections


# Adamın çözdüğü
# Çözüm sayısı 0 | Hedef 5 çözüm
class MinStack(object):
    def __init__(self):
        self.stack = []
        self.min = []
    def push(self, val):
        self.stack.append(val)
        val = min(self.min[-1], val) if self.min else val
        self.min.append(val)
    def pop(self):
        self.stack.pop()
        self.min.pop()
    def top(self):
        return self.stack[-1]
    def getMin(self):
        return self.min[-1]

a = MinStack()
a.push(-2)
a.push(0)
a.push(-3)
print(a.getMin())
a.pop()
print(a.top())
print(a.getMin())
