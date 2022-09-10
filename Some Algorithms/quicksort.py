def quickSort(arr):
    if(len(arr) <= 1):
        return arr
    else:
        pivot = arr.pop()

    items_greater = []
    items_lower = []

    for i in arr:
        if(pivot < i):
            items_greater.append(i)
        else:
            items_lower.append(i)

    return quickSort(items_lower) + [pivot] + quickSort(items_greater)


print(quickSort([12,2,3,1,5,6,70,15,12,3,4]))