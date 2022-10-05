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
    def minDepth(self, root):
        if not root: return 0
        q = collections.deque()
        q.append((root, 1))
        while q:
            firstNode, lvl = q.popleft()
            if not firstNode.left and not firstNode.right: return lvl
            
            if firstNode.left:
                q.append((firstNode.left, lvl + 1))
            if firstNode.right:
                q.append((firstNode.right, lvl + 1))
                
                
            
            
            
                
            
            
            