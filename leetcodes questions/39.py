class Solution(object):
    def combinationSum(self, candidates, target):
        res = []
        
        def backTrack(i, currArr, total):
            if total == target:
                res.append(currArr[:])
                return
            
            if total > target or i == len(candidates): return
            for c in range(i, len(candidates)):
                backTrack(c, currArr + [candidates[c]], total + candidates[c])
        
        backTrack(0, [], 0)
        return res


class Solution(object):
    def combinationSum(self, candidates, target):
        res = []
        
        def backTrack(i, currArr, total):
            if total == target:
                res.append(currArr[:])
                return
            if len(candidates) == i or total > target: return
            
            currArr.append(candidates[i])
            backTrack(i, currArr, total + candidates[i])
            currArr.pop()
            backTrack(i+1, currArr, total)
        
        backTrack(0, [], 0)
        return res