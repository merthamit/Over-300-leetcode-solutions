class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Adamın çözdüğü
# Çözüm sayısı 0 | Hedef 5 çözüm
class Solution(object):
    def maxPathSum(self, root):
        if not root: return
        res = [root.val]
        
        def dfs(root):
            if not root: return 0
            
            left = dfs(root.left)
            right = dfs(root.right)
            leftMax = max(left, 0)
            rightMax = max(right, 0)
            
            res[0] = max(res[0], root.val + leftMax + rightMax)
            
            return root.val + max(leftMax, rightMax)
            
        dfs(root)         
        return res[0]
