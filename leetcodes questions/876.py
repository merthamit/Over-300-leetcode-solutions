# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Adamın çözdüğü
# Çözüm sayısı 0 | Hedef 5 çözüm
class Solution(object):
    def middleNode(self, head):
        mid, right = head, head
        while right and right.next:
            mid = mid.next
            right = right.next.next
        return mid


class Solution(object):
    def middleNode(self, head):
        nums = []
        
        while head:
            nums.append(head)
            head = head.next
        
        return nums[len(nums) // 2]

                        