# Adamın çözdüğü
# Çözüm sayısı 0 | Hedef 5 çözüm
class Solution(object):
    def reverseList(self, head):
        prev, curr = None, head

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        return prev

# nxt = curr.next bölümünde ben burada 1 den sonra gelen 2 nin referansını aldım
# curr.next = prev ' da ise şu anda olan elemanın yani 1 diyelim onun next kısmını prev yaptım yani nxt = curr.next ' de bir şey değişmedi

# Adamın çözdüğü
# Çözüm sayısı 0 | Hedef 5 çözüm
# Recursion
class Solution(object):
    def reverseList(self, head):
        if not head: return None

        newHead = head

        if head.next:
            newHead = self.reverseList(head.next)
            head.next.next = head

        head.next = None

        return newHead