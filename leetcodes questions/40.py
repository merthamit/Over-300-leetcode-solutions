class Solution(object):
    def combinationSum2(self, candidates, target):
        candidates.sort()
        res = []
        def backTrack(i, total, arr):
            if total == target:
                res.append(arr[:])
                return
            
            if total > target or len(candidates) == i: return
            
            arr.append(candidates[i])
            backTrack(i+1, total + candidates[i], arr)
            arr.pop()
            while i+1 < len(candidates) and candidates[i] == candidates[i+1]: i += 1
            backTrack(i+1, total, arr)
            
        
        backTrack(0, 0, [])
        return res

# Adamın çözdüğü
# Çözüm sayısı 0 | Hedef 5 çözüm
class Solution(object):
    def combinationSum2(self, candidates, target):
        candidates.sort()
        res = []
        def backTrack(curr, pos, target):
            if target == 0: res.append(curr[:])
            if target <= 0: return
                
            prev = -1
            for i in range(pos, len(candidates)):
                if candidates[i] == prev:
                    continue
                    
                curr.append(candidates[i])
                backTrack(curr, i+1, target - candidates[i])
                curr.pop()
                prev = candidates[i]
                
        backTrack([], 0, target)
        return res