# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Adamın çözdüğü
# Çözüm sayısı 0 | Hedef 5 çözüm
class Solution(object):
    def isPalindrome(self, head):
        fast, slow = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev = None
        while slow:
            nxt = slow.next
            slow.next = prev
            prev = slow 
            slow = nxt
        
        left, right = head, prev
        while right:
            if left.val != right.val: return False
            left, right = left.next, right.next

        return True

       