# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num):

# class Solution(object):
#     def guessNumber(self, n):
#         left, right = 0, n
        
#         while right >= left:
#             mid = (right+left) // 2
#             myGuess = guess(mid)
#             print(mid)            
#             if(myGuess == 0):
#                 return mid
#             if(myGuess == 1):
#                 left = mid + 1
#             if(myGuess == -1):
#                 right = mid - 1
