from collections import defaultdict

# Adamın çözdüğü
# Çözüm sayısı 0 | Hedef 5 çözüm

class Solution(object):
    def findMinHeightTrees(self, n, edges):
        if n == 1: return [0]
        graph = defaultdict(list)
        
        for i, j in edges:
            graph[j].append(i)
            graph[i].append(j)
        
        
        leaves = [node for node in graph.keys() if len(graph[node]) == 1]
        
        while n > 2:
            n -= len(leaves)
            new_leaves = set()
            for leave in leaves:
                neighbor = graph[leave].pop()
                graph[neighbor].remove(leave)
                
                if len(graph[neighbor]) == 1:
                    new_leaves.add(neighbor)
            
            leaves = new_leaves
        
        return leaves