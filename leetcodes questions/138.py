class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution(object):
    def copyRandomList(self, head):
        dummy = tail = Node(0)
        curr = head
        randomHash = {}
        while curr:
            tail.next = Node(curr.val)
            tail = tail.next
            randomHash[curr] = tail
            curr = curr.next
        
        tail = dummy.next
        while head:
            if head.random: tail.random = randomHash[head.random]
            head = head.next
            tail = tail.next
            
        return dummy.next
            