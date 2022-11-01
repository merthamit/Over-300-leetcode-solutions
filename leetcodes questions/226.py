# Adamın çözdüğü
# Çözüm sayısı 0 | Hedef 5 çözüm
class Solution(object):
    def invertTree(self, root):
        if not root: return root
        stack = [root]
        
        while stack:
            node = stack.pop()
            
            if node:
                stack.append(node.left)
                stack.append(node.right)            
                node.left, node.right = node.right, node.left
        
        return root

# Adamın çözdüğü
# Çözüm sayısı 0 | Hedef 5 çözüm
class Solution(object):
    def invertTree(self, root):
        if not root: return
        
        node1 = self.invertTree(root.left)
        node2 = self.invertTree(root.right)

        root.left, root.right = root.right, root.left
        
        return root
        
        