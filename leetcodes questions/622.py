
# Adamın çözdüğü
# Çözüm sayısı 0 | Hedef 5 çözüm

class ListNode(object):
    def __init__(self, val, next, prev):
        self.val = val
        self.next = next
        self.prev = prev
        
class MyCircularQueue(object):

    def __init__(self, k):
        self.space = k
        self.left = ListNode(0, None, None)
        self.right = ListNode(0, None, self.left)
        self.left.next = self.right

    def enQueue(self, value):
        if self.isFull(): return
        cur = ListNode(value, self.right, self.right.prev)
        self.right.prev.next = cur
        self.right.prev = cur
        self.space -= 1
        return True
    
    def deQueue(self):
        if self.isEmpty(): return
        self.left.next = self.left.next.next
        self.left.next.prev = self.left
        self.space += 1
        return True

    def Front(self):
        if self.isEmpty(): return -1
        return self.left.next.val

    def Rear(self):
        if self.isEmpty(): return -1
        return self.right.prev.val

    def isEmpty(self):
        return self.left.next == self.right
        
    def isFull(self):
        return self.space == 0


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()