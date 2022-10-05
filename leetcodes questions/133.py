
# Definition for a Node.
import collections


class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution(object):
    def cloneGraph(self, node):
        if not node: return node
        
        q = collections.deque()
        q.append(node)
        cloned = {}
        cloned[node] = Node(node.val, [])
        
        while q:
            qNode = q.popleft()
            
            for neighbor in qNode.neighbors:
                if neighbor not in cloned:
                    cloned[neighbor] = Node(neighbor.val, [])
                    q.append(neighbor)
                cloned[qNode].neighbors.append(cloned[neighbor])
        
        return cloned[node]


        