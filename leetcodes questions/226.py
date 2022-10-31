class Solution(object):
    def invertTree(self, root):
        if not root: return
        stack = [root]
        
        while stack:
            node = stack.pop()
            
            if node:
                stack.append(node.left)
                stack.append(node.right)
                self.changePlace(node)
        
        return root
            
    def changePlace(self, root):
        tmp = root.left
        root.left = root.right
        root.right = tmp

class Solution(object):
    def invertTree(self, root):
        if not root: return
        
        node1 = self.invertTree(root.left)
        node2 = self.invertTree(root.right)

        root.left, root.right = root.right, root.left
        
        return root
        
        