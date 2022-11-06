class Solution(object):
    def kthSmallest(self, root, k):
        stack = []
        curr = root
        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
            
            curr = stack.pop()
            k -= 1
            if k == 0: return curr.val
            curr = curr.right
        