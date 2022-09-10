# Başlangıç 19:15
# Bitiş 20:32
# 1 saat 17 dakika
# Kaç tane kaldı ? 0




def binarySearch(arr, target):
    leftIdx, rightIdx = 0, len(arr) -1

    while rightIdx >= leftIdx:
        midIdx = (leftIdx + rightIdx) // 2
        print(f'leftIdx:{leftIdx} || midIdx:{midIdx} || rightIdx:{rightIdx} |||||||| arrMid: {arr[midIdx]}')
        if(arr[midIdx] == target):
            return midIdx
        if(arr[midIdx] > target):
            rightIdx = midIdx - 1
        if(arr[midIdx] < target):
            leftIdx = midIdx + 1
    return -1


a = [1,2,3,4,5]
print(binarySearch(a,55))
