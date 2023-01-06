from collections import defaultdict


class FreqStack(object):

    def __init__(self):
        self.cnt = defaultdict(int)
        self.maxCnt = 0
        self.stack = defaultdict(list)

    def push(self, val):
        valCnt = 1 + self.cnt.get(val, 0)
        self.cnt[val] = valCnt
        self.maxCnt = valCnt if valCnt > self.maxCnt else self.maxCnt
        self.stack[valCnt].append(val)
        
    def pop(self):
        res = self.stack[self.maxCnt].pop()
        self.cnt[res] -= 1
        if not self.stack[self.maxCnt]: self.maxCnt -= 1
        return res
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()