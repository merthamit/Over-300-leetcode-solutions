# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, root, subRoot):
        if not root or not subRoot: return False
        stack = [(root)]
        
        while stack:
            node = stack.pop()
            if node and node.val == subRoot.val:
                if self.isSame(node, subRoot): return True
                
            
            if node:
                stack.append(node.left)
                stack.append(node.right)

        
    def isSame(self, root, subRoot):
        if not root and not subRoot: return True
        if not root or not subRoot: return False
        if root.val != subRoot.val: return False

        return self.isSame(root.left, subRoot.left) and self.isSame(root.right, subRoot.right)


# Adamın çözdüğü
# Çözüm sayısı 0 | Hedef 5 çözüm
class Solution(object):
    def isSubtree(self, root, subRoot):
        if not root: return
        if self.isSame(root, subRoot): return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        
    def isSame(self, root, subRoot):
        if not root and not subRoot: return True
        if not root or not subRoot: return False
        if root.val != subRoot.val: return False

        return self.isSame(root.left, subRoot.left) and self.isSame(root.right, subRoot.right)