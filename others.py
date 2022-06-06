# Neden hızlı yazıyorlar çünkü unutmasınlar diye...
arr = [1,2,3,4,5,6,7,8]
start = 0
end = len(arr) -1

def binary_search(arr, start, end, target):
    middleItemIndex = int((start + end) / 2)
    if(start > end):
        return False
    if(arr[middleItemIndex] == target):
        return True
    if(arr[middleItemIndex] < target):
        return binary_search(arr, middleItemIndex +1, end, target)
    if(arr[middleItemIndex] > target):
        return binary_search(arr, start, middleItemIndex -1, target)


print(binary_search(arr,start,end,4))