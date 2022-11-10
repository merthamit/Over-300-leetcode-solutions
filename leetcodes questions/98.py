# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Adamın çözdüğü
# Çözüm sayısı 0 | Hedef 5 çözüm
class Solution(object):
    def isValidBST(self, root):
        def dfs(node, lower, higher):
            if not node: return True
            
            if not (node.val > lower and node.val < higher): return False
            
            return dfs(node.left, lower, node.val) and dfs(node.right, node.val, higher)
        
        return dfs(root, float('-inf'), float('inf'))