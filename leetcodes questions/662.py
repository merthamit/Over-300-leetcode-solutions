# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections
class Solution(object):
    def widthOfBinaryTree(self, root):
        q = collections.deque([(root, 1)])
        width = 0
        
        while q:
            _,left = q[0]
            _,right = q[-1]
            width = max(width, right - left + 1)
            lng = len(q)
            print(left, right)
            
            for _ in range(lng):
                node, idx = q.popleft()
                
                if node.left:
                    q.append((node.left, idx*2))
                if node.right:
                    q.append((node.right, idx*2+1))
            
                        
        return width
# Also if we give an index to every node, at every level we can calculate the node position/index as follows:
# Left node is positioned at 2i and Right node is positioned at 2i+1 where i is the index of current node we are exploring.n
        
        
        