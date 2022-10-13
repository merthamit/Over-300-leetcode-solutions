import collections


class Solution(object):
    def rightSideView(self, root):
        if not root: return root
        q = collections.deque()
        q.append(root)
        res = []
        
        while q:
            lng = len(q)
            rightSide = None
            for i in range(lng):
                node = q.popleft()
                if node:
                    q.append(node.left)
                    q.append(node.right)
                    rightSide = node
            if rightSide:
                res.append(rightSide.val)
        return res