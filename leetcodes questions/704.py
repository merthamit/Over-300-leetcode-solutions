def binarySearch(nums,target):
    leftIndex = 0
    rightIndex = len(nums) - 1

    while rightIndex >= leftIndex:
        middleIndex = (leftIndex + rightIndex) // 2
        if(nums[middleIndex] == target):
            return middleIndex
        
        elif(nums[middleIndex] < target):
            leftIndex = middleIndex + 1
        elif(nums[middleIndex] > target):
            rightIndex = middleIndex - 1

        print(leftIndex, rightIndex)
    return -1

def binarySearch2(nums,target):
    leftIndex, rightIndex = 0, len(nums) - 1

    while rightIndex >= leftIndex:
        middleIndex = (leftIndex + rightIndex) // 2

        if(nums[middleIndex] == target):
            return middleIndex
        if(nums[middleIndex] < target):
            leftIndex = middleIndex + 1
        if(nums[middleIndex] > target):
            rightIndex = middleIndex -1

    return -1

print(binarySearch2([1,2,3,4,5,6,7,8],5))