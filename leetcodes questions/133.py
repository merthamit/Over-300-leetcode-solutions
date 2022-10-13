
# Definition for a Node.
import collections


class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


# Adamın çözdüğü
# Çözüm sayısı 0 | Hedef 5 çözüm
class Solution(object):
    def cloneGraph(self, node):
        if not node: return node
        q = collections.deque()
        q.append(node)
        cloned = {}
        cloned[node] = Node(node.val, [])

        while q:
            qNode = q.popleft()

            for i in qNode.neighbors:
                if i not in cloned:
                    cloned[i] = Node(i.val, [])
                    q.append(i)
                cloned[qNode].neighbors.append(cloned[i])
        
        return cloned[node]