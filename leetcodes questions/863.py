# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import collections


class Solution(object):
    def distanceK(self, root, target, k):
        if not root: return root
        graph = collections.defaultdict(list)
        q = collections.deque()
        q.append(root)
        
        while q:
            node = q.popleft()
            
            if node.left:
                q.append(node.left)
                graph[node].append(node.left)
                graph[node.left].append(node)
            if node.right:
                q.append(node.right)
                graph[node].append(node.right)
                graph[node.right].append(node)
                
        distance = 0
        q2 = collections.deque([target])
        visit = set()
        visit.add(target)
        res = []
        while q2 and distance <= k:
            lng = len(q2)
            for _ in range(lng):
                node = q2.popleft()
                
                if distance == k:
                    res.append(node.val)
                
                for neighbor in graph[node]:
                    if neighbor not in visit:
                        visit.add(node)
                        q2.append(neighbor)
                
            distance += 1
            
        return res
                        
            
                
                
                
            
                    
        
    
        