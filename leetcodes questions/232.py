# Adamın çözdüğü
# Çözüm sayısı 0 | Hedef 5 çözüm
class MyQueue(object):

    def __init__(self):
        self.popS = []
        self.pushS = []

    def push(self, x):
        self.pushS.append(x)

    def converToPopS(self):
        while self.pushS:
            self.popS.append(self.pushS.pop())
        
    def pop(self):
        if not self.popS:
            self.converToPopS()
        return self.popS.pop()

    def peek(self):
        if not self.popS:
            self.converToPopS()
        return self.popS[-1]

    def empty(self):
        return len(self.popS) == 0 and len(self.pushS) == 0

myQueue = MyQueue()
myQueue.push(1)
myQueue.push(2)
print(myQueue.peek())
myQueue.pop()
print(myQueue.empty())