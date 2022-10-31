class Solution(object):
    def pathSum(self, root, targetSum):
        if not root: return root
        res, stack = [], [(root, targetSum - root.val, [root.val])]

        while stack:
            node, total, arr = stack.pop()
            if not (node.left or node.right or total):
                res.append(arr)
                
            if node.left:
                newArr = arr + [node.left.val]
                stack.append((node.left, total - node.left.val, newArr))
                
            if node.right:
                newArr = arr + [node.right.val]
                stack.append((node.right, total - node.right.val, newArr))
        
        return res
        
class Solution(object):
    def pathSum(self, root, targetSum):
        if not root: return root
        res = []
        
        def dfs(root, total, arr):
            if not root: return
            newArr = [i for i in arr]
            newArr.append(root.val)
            total += root.val 
            
            if not root.right and not root.left:
                if total == targetSum: res.append(newArr)
                    
            
            return dfs(root.left, total, newArr) or dfs(root.right, total, newArr)
        
        dfs(root, 0, [])
        
        return res
                