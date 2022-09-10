def isPowerOfTwo(num):
    if(num == 1 or num == 2):
        return True
    if(num % 2 == 0 and num != 0):
        return isPowerOfTwo(int(num / 2))
    else:
        return False


def fib(num, cache = {}):
    cacheFile = cache
    if(num in cacheFile):
        return cacheFile[num]
    if(num in [0,1]):
        return num
    cacheFile[num] = fib(num - 2, cacheFile) + fib(num - 1, cacheFile)
    return cacheFile[num]

def reverseString(s):
    s.reverse()
    return s

def strStr(haystack, needle):
    word = {
        'firstSeen': 0,
        'word': '',
        'indexes': {}
    }
    for idx, i in enumerate(haystack):
        if(haystack[idx] == needle[0]):
            word['indexes'][idx] = haystack[idx : idx + len(needle)]
    for i in word['indexes'].keys():
        if(word['indexes'][i] == needle):
            return i
    return -1


class Solution(object):
    def strStr(self,haystack, needle):
        for idx, i in enumerate(haystack):
            if(haystack[idx] == needle[0]):
                if(haystack[idx : idx + len(needle)] == needle):
                    return idx 
        return -1


def something(arr):
    i = len(arr)-1
    j = i
    count = 0
    while True:
        j = i
        while True:
            print(arr[i], arr[j])
            count = count + 1
            if(j < 1):
                break
            j = j -1
        if(i < 1):
            break
        i -=1
    print(count)
    


def findTheDistanceValue(arr1,arr2,d):
    count = []
    for idx,i in enumerate(arr1):
        count.append(idx)
        for j in arr2:
            val = 0
            if((i - j) <= 0):
                val = -1 *(i - j)
            else:
                val = i - j
            if(val <= d or val == d):
                count.pop()
                break
    return len(count)                
            
        

class Solution(object):
    def total(self, arr):
        newBucket = [1]
        if(len(arr) == 1):
            return 1
        for idx, i in enumerate(arr):
            if(len(arr) == (idx + 1)):
                newBucket.append(1)
                return newBucket
            total = arr[idx] + arr[idx+1]
            newBucket.append(total)

    # def generate(self, numRows):
    #     res = [[1]]
    #     for i in range(1, numRows):
    #         res.append(list(map(lambda x, y: x+y, res[-1] + [0], [0] + res[-1])))
    #     return res

    def generate(self, numRows):
        bucket = []
        if(numRows == 1):
            return [[1]]
        for i in range(1,numRows):
            if(len(bucket) == 0):
                bucket.append([1])
                bucket.append([1,1])
                continue
            beforeEl = self.total(bucket[i-1])
            bucket.append(beforeEl)
        return bucket

a = Solution()
b = [1,3,3,1,0] 
# Aslında minik matematik numaraları var ve onu görmek lazım easylerde sende onu gör...
d = [0,1,3,3,1]
c = list(map(lambda x,y: x+y,b,d))



class Solution(object):
    def search(self, nums, target):
        arrLen = len(nums)
        while True:
            if(arrLen == 0 or (arrLen / 2 > len(nums))):
                return -1
            middleNum = nums[int(arrLen / 2)]
            if(middleNum == target):
                return int(arrLen / 2 )         
            if(target > middleNum):
                arrLen = arrLen * 2 -1
                print(arrLen)
            if(target < middleNum):
                arrLen = int(arrLen / 2)
            
a = Solution()
print(a.search([-1,0,3,5,9,12],9))