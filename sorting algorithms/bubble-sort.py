# Best case o(n^2) eğer isSort kontrolü yaparsak best case o(n)
# Average case o(n^2)
# Worst case o(n^2)

def bubbleSort(arr):
    dataLen = len(arr) -1
    while dataLen >= 0:
        for index in range(0, dataLen):
            value = arr[index]
            if(arr[index] > arr[index+1]):
                print(arr)
                arr[index] = arr[index+1]
                arr[index+1] = value
        dataLen -= 1
    return arr

def bubbleSort2(arr):
    for dataLen in range(len(arr)-1,0, -1):
        isSort = True
        for index in range(dataLen):
            if(arr[index] > arr[index + 1]):
                isSort = False
                tmp = arr[index]
                arr[index] = arr[index + 1]
                arr[index + 1] = tmp
        if(isSort):
            print('Sirali')
            break
    return arr
print(bubbleSort2([1,2,3,4,5]))