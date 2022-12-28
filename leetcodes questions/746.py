class Solution(object):
    def minCostClimbingStairs(self, cost):
        for i in range(len(cost)-3, -1, -1):
            minStep = min(cost[i+1], cost[i+2])
            cost[i] += minStep
        
        return min(cost[0], cost[1])
        