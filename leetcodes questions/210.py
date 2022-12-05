import collections

class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        if numCourses <= 1: return [0]
        preMap = collections.defaultdict(list)
        res = []
        for a, b in prerequisites:
            preMap[a].append(b)
        
        cycle, courseQ = set(), set()
        def dfs(crs):
            if crs in cycle: return False
            if not preMap[crs]: 
                if crs not in courseQ:
                    courseQ.add(crs)
                    res.append(crs)
                return True
            
            cycle.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre): return False
            cycle.remove(crs)
            res.append(crs)
            courseQ.add(crs)
            preMap[crs] = []
            
            
            return True
        
        for i in range(numCourses):
            if not dfs(i): return []
            
        return res

# Adamın çözdüğü
# Çözüm sayısı 0 | Hedef 5 çözüm
class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        preMap = collections.defaultdict(list)
        res = []
        for a, b in prerequisites:
            preMap[a].append(b)
        
        cycle, visit = set(), set()
        def dfs(crs):
            if crs in cycle: return False
            if crs in visit: return True
            
            cycle.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre): return False
            cycle.remove(crs)
            res.append(crs)
            visit.add(crs)
            
            return True
        
        for i in range(numCourses):
            if not dfs(i): return []
            
        return res