# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# Benim çözdüğüm
# Çözüm sayısı 0 | Hedef 5 çözüm
class Solution(object):
    def deleteNode(self, node):
        node.val = node.next.val
        node.next = node.next.next