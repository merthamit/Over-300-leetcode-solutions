# Adamın çözdüğü
# Çözüm sayısı 0 | Hedef 5 çözüm

class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None

class MyLinkedList(object):
    def __init__(self):
        self.head = None
        self.size = 0
    
    def get(self, index):
        if index >= self.size: return -1

        curr = self.head
        while index:
            curr = curr.next
            index -= 1

        return curr.val

    def addAtHead(self, val):
        self.addAtIndex(0, val)

    def addAtTail(self, val):
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index, val):
        if index > self.size: return
        curr = self.head
        newNode = ListNode(val)

        if index <= 0:
            newNode.next = curr
            self.head = newNode
        else:
            while index-1:
                curr = curr.next
                index -= 1
            
            nxt = curr.next
            newNode.next = nxt
            curr.next = newNode

        self.size += 1

    def deleteAtIndex(self, index):
        if index >= self.size: return
        curr = self.head

        if index <= 0:
            self.head = self.head.next
        else:
            while index-1:
                curr = curr.next
                index -= 1
            
            curr.next = curr.next.next
        
        self.size -= 1

a = MyLinkedList()
a.addAtHead(5)
print(a.get(0))

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)