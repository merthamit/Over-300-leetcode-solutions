class Solution(object):
    def goodNodes(self, root):
        if not root: return 0
        
        stack = [(root, root.val)]
        count = 0
        while stack:
            node, maxN = stack.pop()
            
            if node.val >= maxN:
                maxN = node.val
                count += 1
            
            if node.left:
                stack.append((node.left, maxN))
            if node.right:
                stack.append((node.right, maxN))
        
        return count

class Solution(object):
    def goodNodes(self, root):
        if not root: return 0
        
        def dfs(root, maxVal):
            if not root: return 0
            
            res = 1 if root.val >= maxVal else 0
            maxVal = max(maxVal, root.val)
            res += dfs(root.left, maxVal)
            res += dfs(root.right, maxVal)
            
            return res
        
        return dfs(root, root.val)