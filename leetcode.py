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
            
        
print(findTheDistanceValue([2,1,100,3],[-5,-2,10,-3,7],6))


    # for idx,i in enumerate(arr1):
    #     count.append(idx)
    #     for j in arr2:
    #         val = 0
    #         if((i - j) <= 0):
    #             val = -1 *(i - j)
    #         else:
    #             val = i - j
    #         if(val <= d or val == d):
    #             count.pop()
    #             break
    # return len(count)