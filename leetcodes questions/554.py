class Solution(object):
    def leastBricks(self, wall):
        countGap = { 0 : 0 }
        
        for bricks in wall:
            total = 0
            for brick in bricks[:-1]:
                total += brick
                countGap[total] = 1 + countGap.get(total, 0)
                
        return len(wall) - max(countGap.values())
            
        