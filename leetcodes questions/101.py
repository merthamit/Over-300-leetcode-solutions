# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        if not (root.left or root.right): return True
        stack = [(root.left, root.right)]
        while stack:
            first, second = stack.pop()
            
            if not first and not second: pass
            elif not first or not second: return False
            else:
                if first.val != second.val: return False
                stack.append((first.left, second.right))
                stack.append((first.right, second.left))

        return True


class Solution(object):
    def isSymmetric(self, root):
        
        def dfs(node1, node2):
            if not node1 and not node2: return True
            if not node1 or not node2: return False
            if node1.val != node2.val: return False
            
            return dfs(node1.left, node2.right) and dfs(node2.left, node1.right)

        return dfs(root.left, root.right)