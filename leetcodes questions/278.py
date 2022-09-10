class Solution(object):
    def firstBadVersion(self, n):
        left, right = 1, n

        
        while right >= left:
            mid = (right + left) //  2
            isBad = isBadVersion(mid)
            if(isBad):
                right = mid -1
            if(not isBad):
                left = mid + 1
            if(right < left):
                return left
            print(left, right)
