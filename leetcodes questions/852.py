class Solution(object):
    def peakIndexInMountainArray(self, arr):
        leftIndex = 0
        rightIndex = len(arr) - 1
        
        while rightIndex >= leftIndex:
            middleIndex = (leftIndex + rightIndex) // 2
            if(arr[middleIndex] > arr[middleIndex -1] and arr[middleIndex] > arr[middleIndex + 1]):
                return middleIndex
            if(arr[middleIndex - 1] > arr[middleIndex + 1]):
                rightIndex = middleIndex - 1
            if(arr[middleIndex + 1] > arr[middleIndex -1]):
                leftIndex = middleIndex + 1



print(Solution().peakIndexInMountainArray([3,4,5,1]))