# Chunk edilecek çözüm...
class ChunkSolution(object):
    def searchInsert(self, nums, target):
        leftIdx, rightIdx = 0, len(nums) - 1
        while rightIdx >= leftIdx:
            midIdx = (rightIdx + leftIdx) // 2
            print(f'leftIdx:{leftIdx} || midIdx:{midIdx} || rightIdx:{rightIdx} ||||||||')
            if(nums[midIdx] == target):
                return midIdx
            if(nums[midIdx] < target):
                leftIdx = midIdx + 1
            if(nums[midIdx] > target):
                rightIdx = rightIdx - 1
        print(f'leftIdx:{leftIdx} || midIdx:{midIdx} || rightIdx:{rightIdx} ||||||||')
        
        return leftIdx
print(ChunkSolution().searchInsert([1],-2))


# Neredeyse aynılar...


# Benim çözümüm
class Solution(object):
    def searchInsert(self, nums, target):
        leftIdx, rightIdx = 0, len(nums) - 1
        while rightIdx >= leftIdx:
            midIdx = (rightIdx + leftIdx) // 2
            if(nums[midIdx] == target):
                return midIdx
            if(midIdx == rightIdx == leftIdx):
                if(midIdx + 1 == len(nums) and nums[midIdx] < target):
                    midIdx += 1
                return midIdx
            if(nums[midIdx] < target):
                leftIdx = midIdx + 1
            if(nums[midIdx] > target):
                rightIdx = rightIdx - 1
        return False



