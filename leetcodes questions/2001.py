class Solution(object):
    def interchangeableRectangles(self, rectangles):
        rectangleHash, res = {}, 0
        
        for w, h in rectangles:
            rectangleHash[(float(w) / h)] = 1 + rectangleHash.get((float(w) / h), 0)
            
        for w, h in rectangles:
            rectangleHash[(float(w) / h)] -= 1
            res += rectangleHash[(float(w) / h)]
        
        return res

class Solution(object):
    def interchangeableRectangles(self, rectangles):
        rectangleHash, res = {}, 0
        
        for w, h in rectangles:
            rectangleHash[(float(w) / h)] = 1 + rectangleHash.get((float(w) / h), 0)
            
        for c in rectangleHash.values():
            if c > 1:
                res += (c * (c - 1)) // 2 # --> 2 ye bölğyor çünkü duplicateleri alıyor.
        
        return res