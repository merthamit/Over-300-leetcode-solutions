# Adamın çözdüğü
# Çözüm sayısı 0 | Hedef 5 çözüm
class Solution(object):
    def inorderTraversal(self, root):
        res = []
        def inorder(root):
            if not root: return
            inorder(root.left)
            res.append(root.val)
            inorder(root.right)
        inorder(root)
        return res
# Adamın çözdüğü
# Çözüm sayısı 0 | Hedef 5 çözüm
class Solution(object):
    def inorderTraversal(self, root):
        stack, output = [], []
        curr = root
        
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            
            curr = stack.pop()
            output.append(curr.val)
            curr = curr.right
        
        return output
                