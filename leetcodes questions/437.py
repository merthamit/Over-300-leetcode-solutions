# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections
class Solution(object):
    def pathSum(self, root, targetSum):
        res = [0]
        def newDfs(root, targetSum):
            if not root: return 0
            
            res[0] += self.dfs(root, 0, targetSum)
        
            return newDfs(root.left, targetSum) + newDfs(root.right, targetSum)
        
        newDfs(root, targetSum)
        return res[0]
        
    def dfs(self, root, total, targetSum):
        if not root: return 0

        total += root.val

        res = 1 if total == targetSum else 0
        res += self.dfs(root.left, total, targetSum)
        res += self.dfs(root.right, total, targetSum)

        return res
        
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        self.lookup = collections.defaultdict(int)
        self.lookup[targetSum] = 1
        self.total = 0
        
        def dfs(node, rootSum):
            if not node: return
            
            rootSum += node.val
            self.total += self.lookup[rootSum]
            self.lookup[rootSum + targetSum] += 1
            dfs(node.left, rootSum)
            dfs(node.right, rootSum)
            self.lookup[rootSum + targetSum] -= 1
        
        dfs(root, 0)    
        return self.total

# Adamın çözdüğü
# Çözüm sayısı 0 | Hedef 5 çözüm
class Solution(object):
    def pathSum(self, root, targetSum):
        self.res = 0
        self.lookup = collections.defaultdict(int)
        self.lookup[0] = 1
        
        def dfs(root, rootSum):
            if not root: return
            
            rootSum += root.val
            self.res += self.lookup[rootSum - targetSum]
            self.lookup[rootSum] += 1
            
            dfs(root.left, rootSum)
            dfs(root.right, rootSum)
            
            self.lookup[rootSum] -= 1
            
        dfs(root, 0)
        return self.res
        
# https://medium.com/geekculture/path-sum-iii-leetcode-437-588d8e56acac
class Solution(object):
    def pathSum(self, root, targetSum):
        self.count = 0
        summ = 0
        sumMap = collections.defaultdict(int)

        def traverseTree(curr, summ):
            if not curr:
                return
            
            summ += curr.val
            
            if summ == targetSum :
                self.count += 1

            self.count += sumMap.get(summ - targetSum, 0)

            sumMap[summ] += 1
            
            traverseTree(curr.left, summ)
            traverseTree(curr.right, summ)

            if sumMap.get(summ):
                sumMap[summ] -= 1
                
        traverseTree(root, 0)
        return self.count