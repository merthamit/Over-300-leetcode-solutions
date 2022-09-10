# Chunk edilecek çözüm
class Solution(object):
    def isPerfectSquare(self, num):
        left, right = 0, num - 1

        if(num == 1):
            return True

        while right >= left:
            mid = (left + right) // 2
            print(f'leftIdx:{left} || mid:{mid} || right:{right} ||||||||')
            if(mid * mid == num):
                return True
            if(mid * mid > num):
                right = mid - 1
            if(mid * mid < num):
                left = mid + 1
        
        return False
        

print(Solution().isPerfectSquare(16))