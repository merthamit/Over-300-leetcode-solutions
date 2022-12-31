# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Adamın çözdüğü
# Çözüm sayısı 0 | Hedef 5 çözüm
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        l1, l2 = headA, headB
        while l1 != l2:
            l1 = l1.next if l1 else headB
            l2 = l2.next if l2 else headA
        return l1
        
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        currA, currB = headA, headB
        lengthA, lengthB = 0, 0
        
        while currA or currB:
            if currA:
                currA = currA.next
                lengthA += 1
            if currB:
                currB = currB.next
                lengthB += 1
            
        delta = abs(lengthA - lengthB)

        currA, currB = headA, headB
        if lengthB > lengthA:
            while currB and delta:
                currB = currB.next
                delta -= 1
        else:
            while currA and delta:
                currA = currA.next
                delta -= 1

        while currA != currB:
            currA = currA.next if currA else None
            currB = currB.next if currB else None
        
        return currA
# l1 ve l2 eşit olunca return l1 oluyor ve eğer kesiştiği yer yoksa bu sefer None da buluşacaklar ve l1 None olacak dönecek
print(Solution().getIntersectionNode())