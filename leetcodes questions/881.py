class Solution(object):
    def numRescueBoats(self, people, limit):
        people.sort()
        l, r = 0, len(people) - 1
        res = 0
        
        while r >= l:
            remain = limit - people[r]
            res += 1
            r -= 1
            
            if r >= l and people[l] <= remain:
                l += 1
        return res