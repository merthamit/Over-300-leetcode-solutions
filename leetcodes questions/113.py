# Adamın çözdüğü
# Çözüm sayısı 0 | Hedef 5 çözüm
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
# Adamın çözdüğü
# Çözüm sayısı 1 | Hedef 5 çözüm
class Solution(object):
    def pathSum(self, root, targetSum):
        if not root: return root
        res = []
        def dfs(root, total, arr):
            if not root: return 

            newArr = arr + [root.val]
            total += root.val

            if not root.left and not root.right:
                if total == targetSum: res.append(newArr)


            return dfs(root.left, total, newArr) or dfs(root.right, total, newArr)

        dfs(root, 0, [])

        return res
