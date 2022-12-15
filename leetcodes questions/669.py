# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def trimBST(self, root, low, high):
        if not root: return root
        
        if root.val > high:
            #root.left çünkü sağdakide highdan büyük olacak
            return self.trimBST(root.left, low, high)
        if root.val < low:
            #root.right çünkü soldakide lowdan küçük olacak
            return self.trimBST(root.right, low, high)
         
        root.left = self.trimBST(root.left, low, high)
        root.right = self.trimBST(root.right, low, high)
        
        return root

