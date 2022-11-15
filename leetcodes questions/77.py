class Solution(object):
    def combine(self, n, k):
        arr = [i for i in range(1,n+1)]
        res = []
        def backTrack(i, currArr):
            if len(currArr) == k:
                res.append(currArr[:])
                return
            if len(arr) == i: return
            
            for j in range(i, len(arr)):
                backTrack(j+1, currArr + [arr[j]])
                
        backTrack(0, [])
        return res

class Solution(object):
    def combine(self, n, k):
        res = []
        def backTrack(start, comb):
            if len(comb) == k:
                res.append(comb[:])
                return
            
            for j in range(start, n+1):
                comb.append(j)
                backTrack(j+1, comb)
                comb.pop()
                
        backTrack(1, [])
        return res