from typing import final


def twoSum(nums, target):
    holdArr = {}
    for idx, i in enumerate(nums):
        print(holdArr)
        tMinus = target - i
        if(i in holdArr):
            return [holdArr[i],idx]
        else:
            holdArr[tMinus] = idx
    print(holdArr)
    return False

class Solution(object):
    def twoSum(self, nums, target):
        numsObj = {}
        for idx, i in enumerate(nums):
            targetMinusNum = target - i
            numsObj[targetMinusNum] = idx

        for jdx, j in enumerate(nums):
            try:
                if(numsObj[j] and jdx != numsObj[j]):
                    return [jdx, numsObj[j]]
            except:
                continue

        return numsObj               
            
            
# class Solution(object):
#     def twoSum(self,nums, target):
#         holdArr = {}
#         arr = []
#         for idx, i in enumerate(nums):
#             tMinus = target - i
#             try:
#                 if(holdArr[i]):
#                     print('dsf')
#             except:
#                 holdArr[tMinus] = idx
#                 continue
#             if(str(holdArr[i]) and holdArr[i] != idx):
#                 print(holdArr)
#                 arr.append(holdArr[i])
#                 arr.append(idx)
#                 break
#         return arr


p1 = Solution()
print(p1.twoSum([2,7],9)) 


# print(twoSum([4,5,7,1], 12))
