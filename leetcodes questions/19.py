# Adamın çözdüğü
# Çözüm sayısı 0 | Hedef 5 çözüm
class ListNode(object):
    def __init__(self):
        return ''

class Solution(object):
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(None, head)
        left, right = dummy, head

        while n:
            n -= 1
            right = right.next

        while right:
            left = left.next
            right = right.next
        
        left.next = left.next.next

        return dummy.next
        