import collections

class Solution(object):
    def eventualSafeNodes(self, graph):
        n = len(graph)
        res, safe = [], {}
        
        def dfs(i):
            if i in safe: return safe[i]
            safe[i] = False
            
            for nei in graph[i]:
                if not dfs(nei): return safe[i]
                
            safe[i] = True
            return safe[i]
            
        
        for i in range(n):
            if dfs(i): res.append(i)
        
        return res
            
            
            

class Solution(object):
    def eventualSafeNodes(self, graph):
        graphList = collections.defaultdict(list)
        res = []
        
        for i, a in enumerate(graph):
            if a:
                for g in a:
                    graphList[i].append(g)
            else:
                graphList[i] = []
                
        cycle = set()
        def dfs(stt):
            if stt in cycle: return False
            if not graphList[stt]: return True
            
            cycle.add(stt)
            for i in graphList[stt]:
                if not dfs(i): return False

            cycle.remove(stt)
            graphList[stt] = []
            
            return True
        
        
        for i in range(0, len(graph)):
            if dfs(i): res.append(i)
        
        return res
            
            
            
