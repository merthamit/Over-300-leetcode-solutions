# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Adamın çözdüğü
# Çözüm sayısı 0 | Hedef 5 çözüm
class Solution(object):
    def rob(self, root):
        
        def dfs(root):
            if not root: return [0, 0]
            
            left = dfs(root.left)
            right = dfs(root.right)
            
            withRoot = root.val + left[1] + right[1]
            withOutRoot = max(left) + max(right)
            
            return [withRoot, withOutRoot]
        
        return max(dfs(root))
            
            