# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        dummy = ListNode(0, head)
        curr, leftPrev = head, dummy
        
        for i in range(left-1):
            curr, leftPrev = curr.next, curr
        
        prev = None
        for i in range(right - left + 1):
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        leftPrev.next.next = curr
        leftPrev.next = prev
        
        return dummy.next
        