# Adamın çözdüğü
# Çözüm sayısı 0 | Hedef 5 çözüm
class Solution(object):
    def detectCycle(self, head):
        if not head: return None
        
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast: break

        slow2 = head
        while slow.next:
            if slow == slow2: return slow
            slow = slow.next
            slow2 = slow2.next
        
        return None
