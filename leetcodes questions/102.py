# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections


class Solution(object):
    def levelOrder(self, root):
        if not root: return root
        res = []
        q = collections.deque()
        q.append(root)
        
        while q:
            lng = len(q)
            total = []
            
            for i in range(lng):
                node = q.popleft()
                total.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            res.append(total)
        
        return res

class Solution(object):
    def levelOrder(self, root):
        if not root: return root
        res = []
        q = collections.deque()
        q.append(root)
        
        while q:
            lng = len(q)
            total = []
            
            for i in range(lng):
                node = q.popleft()
                if node:
                    total.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            
            if total:
                res.append(total)
        
        return res