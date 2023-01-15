# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def convertBST(self, root):
        currSum = [0]
        
        def dfs(node):
            if not node: return
            
            dfs(node.right)
            tmp = node.val
            node.val += currSum[0]
            currSum[0] += tmp
            dfs(node.left)
        
        dfs(root)
        return root