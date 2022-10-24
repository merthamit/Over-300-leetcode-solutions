# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        if not root: return 0
        
        stack = [(root, 1)]
        maxDepth = 0
        while stack:
            node, depth = stack.pop()
            if node:
                maxDepth = max(maxDepth, depth)
                stack.append((node.left, depth + 1))
                stack.append((node.right, depth + 1))
        
        return maxDepth

class Solution(object):
    def maxDepth(self, root):
        if not root: return 0
        
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
            
            
        