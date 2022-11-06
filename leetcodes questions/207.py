from collections import defaultdict
# Adamın çözdüğü
# Çözüm sayısı 0 | Hedef 5 çözüm
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        preMap = defaultdict(list)
        
        for a, b in prerequisites:
            preMap[a].append(b)
            
        visit = set()
        def dfs(crs):
            if crs in visit: return False
            if not preMap[crs]: return True
            
            visit.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre): return False
            visit.remove(crs)
            preMap[crs] = []
            return True
        
        for i in range(numCourses):
            if not dfs(i): return False
        
        return True
                
            
print(Solution().canFinish(2,[[0,1],[1,0]]))
            