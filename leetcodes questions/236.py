# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        def dfs(root):
            if not root: return
            
            if root == p or root == q: return root
            
            left = dfs(root.left)
            right = dfs(root.right)
            
            if left and right: return root
            
            return left if left else right
        
        return dfs(root)