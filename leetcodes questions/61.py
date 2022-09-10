# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Adamın çözdüğü
# Çözüm sayısı 0 | Hedef 5 çözüm
class Solution(object):
    def rotateRight(self, head, k):
        if not head: return head
        length, tail = 1, head

        while tail.next:
            tail = tail.next
            length += 1
        
        curr = head
        k = k % length
        if k == 0: return head

        for i in range(length - k - 1):
            curr = curr.next

        newHead = curr.next
        curr.next = None
        tail.next = head
        return newHead
