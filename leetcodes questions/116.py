"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

import collections


class Solution(object):
    def connect(self, root):
        if not root: return root
        q = collections.deque([root])
        
        while q:
            qLen = len(q)
            
            for i in range(qLen):
                node = q.popleft()
                
                if i + 1 < qLen:
                    node.next = q[0]
                    
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        
        return root

# O(n) time 
# O(1) space
class Solution(object):
    def connect(self, root):
        if not root: return root
        curr, nxt = root, root.left if root else None
        
        while curr and nxt:
            curr.left.next = curr.right
            
            if curr.next:
                curr.right.next = curr.next.left
            
            curr = curr.next
            if not curr:
                curr = nxt
                nxt = curr.left
        
        return root