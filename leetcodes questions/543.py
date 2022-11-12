class Solution(object):
    def diameterOfBinaryTree(self, root):
        if not root: return 0
        output = 0
        def dfs(root, depth):
            if not root: return 0
            if not root.left and not root.right:
                return depth
            
            return max(dfs(root.left, depth + 1),dfs(root.right, depth + 1))

        stack = [(root, 0)]
        
        while stack:
            node, depth = stack.pop()
            l, r = 0, 0
            
            if node.left:
                stack.append((node.left, depth + 1))
                l = dfs(node.left, 1)
            if node.right:
                stack.append((node.right, depth + 1))
                r = dfs(node.right, 1)
            
            output = max(output, l + r)

                
        return output


# Adamın çözdüğü
# Çözüm sayısı 0 | Hedef 5 çözüm
class Solution(object):
    def diameterOfBinaryTree(self, root):
        res = [0]
        
        def dfs(root):
            if not root: return 0
            
            left = dfs(root.left)
            right = dfs(root.right)
            
            res[0] = max(res[0], left + right)
            return 1 + max(left, right)
        
        dfs(root)
        
        return res[0]
    
            