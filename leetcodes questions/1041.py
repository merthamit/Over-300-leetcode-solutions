class Solution(object):
    def isRobotBounded(self, instructions):
        dirX, dirY = 0, 1
        x, y = 0, 0
        
        for d in instructions:
            if d == 'G':
                x, y = dirX + x, dirY + y
            elif d == 'L':
                dirX, dirY = dirY*-1, dirX
            else:
                dirX, dirY = dirY, dirX*-1
                
        return (x, y) == (0, 0) or (dirX, dirY) != (0, 1)