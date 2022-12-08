import collections
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Adamın çözdüğü
# Çözüm sayısı 0 | Hedef 5 çözüm
class Solution(object):
    def findBottomLeftValue(self, root):
        q = collections.deque([root])
        
        while q:
            node = q.popleft()
            if node.right: q.append(node.right)
            if node.left: q.append(node.left)
             
        return node.val