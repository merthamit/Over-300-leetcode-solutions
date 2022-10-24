class Solution(object):
    def hasPathSum(self, root, targetSum):
        if not root: return False
        stack = [(root, targetSum - root.val)]
        while stack:
            node, rest = stack.pop()
            
            if not (node.left or node.right or rest):
                return True
            
            if node.left:
                stack.append((node.left, rest - node.left.val))
            if node.right:
                stack.append((node.right, rest - node.right.val))
             
        return False

class Solution(object):
    def hasPathSum(self, root, targetSum):
        if not root: return
        
        def dfs(node, currSum):
            if not node: return
            
            currSum += node.val
            if not node.left and not node.right:
                return currSum == targetSum
            
            return dfs(node.left, currSum) or dfs(node.right, currSum)
        
        return dfs(root, 0)
        