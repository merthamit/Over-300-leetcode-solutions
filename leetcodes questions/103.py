# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections


class Solution(object):
    def zigzagLevelOrder(self, root):
        if not root: return root
        res = []
        q = collections.deque()
        q.append(root)
        zigzag = True
        
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
            zigzag = not zigzag
            res.append(total[::-1] if zigzag else total)
        return res
