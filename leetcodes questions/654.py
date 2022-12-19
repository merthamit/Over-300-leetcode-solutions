# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        self.numsIdx = { n: i for i, n in enumerate(nums) }
        def dfs(l, r):
            if l > r: return
            maxNum = max(nums[l:r+1])
            maxNumIdx = self.numsIdx[maxNum]
            
            node = TreeNode(maxNum)
            node.left = dfs(l, maxNumIdx-1)
            node.right = dfs(maxNumIdx+1, r)
            
            return node
        
        return dfs(0, len(nums)-1)

class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        if not nums:
            return None
        stack = []  
        for i in nums:
            node = TreeNode(i)
            lastpop = None
            
            while stack and stack[-1].val < i:
                lastpop = stack.pop()
            node.left = lastpop
            
            if stack:
                stack[-1].right = node
            stack.append(node)
            
        return stack[0]