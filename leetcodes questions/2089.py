class Solution(object):
    def targetIndices(self, nums, target):
        lenData, allIdx= len(nums) -1, []
        while lenData >= 0:
            for idx in range(lenData):
                value = nums[idx]
                if(nums[idx] > nums[idx+1]):
                    nums[idx] = nums[idx +1]
                    nums[idx + 1] = value
            lenData -= 1    
        

        for idx, i in enumerate(nums):
            if(i == target):
                allIdx.append(idx)
        return allIdx


        # print(nums)
        # while rightIdx >= leftIdx:
        #     midIdx = (leftIdx + rightIdx) // 2
        #     print(f'leftIdx:{leftIdx} || midIdx:{midIdx} || rightIdx:{rightIdx} |||||||| arrMid: {nums[midIdx]}')
        #     if(nums[midIdx] == target):
        #         allIdx.append(midIdx)
        #         break
        #     if(nums[midIdx] > target):
        #         rightIdx = midIdx - 1
        #     if(nums[midIdx] < target):
        #         leftIdx = midIdx + 1
        # return allIdx

print(Solution().targetIndices([1,2,5,2,3],2))



