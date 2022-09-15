class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Adamın çözdüğü
# Çözüm sayısı 0 | Hedef 5 çözüm
class Solution(object):
    def deleteDuplicates(self, head):
        curr = head

        while curr:
            while curr.next and curr.val == curr.next.val:
                curr.next = curr.next.next
            
            curr = curr.next
        
        return head