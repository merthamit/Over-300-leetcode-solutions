# Best case o(n)
# Average case o(n^2)
# Worst case o(n^2)

def insertionSort(arr):
    i = 0
    k = i - 1
    while i < len(arr):
        m = i
        j = m - 1
        if(arr[i] < arr[k] and k > -1):
            while m > 0:
                if(arr[m] < arr[j] and j > -1):
                    print(arr)
                    print(f'i = {i} -- arr {arr[i]} -- k = {k} -- arr {arr[k]} |||| m = {m} -- arr {arr[m]} -- j = {j} -- arr {arr[j]}')
                    tmp = arr[j]
                    arr[j] = arr[m]
                    arr[m] = tmp
                m -= 1
                if(m == 0):
                    print(f'm = 0 ve bitti')
                j -= 1
        i += 1
        k += 1
    return arr

def insertionSort2(arr):
    for index in range(1,len(arr)):
        #  1.işlem Burada 1.indexdeki 6 sayısını tuttu
        #  2.işlem Burada 2.indexdeki 1 sayısını tuttu
        value = arr[index]
        #  1.işlem burada 0.indexdeki 4 sayısını tuttu
        #  2.işlem burada 1.indexdeki 6 sayısını tuttu
        leftIndex = index - 1
        #  1.işlem burada 0.indexdeki sayı 1.indexdeki sayıdan büyük mü diye sordu false aldı
        #  2.işlem burada 1.indexdeki sayı 2.indexdeki sayıdan büyük mü diye sordu true aldı
        if(arr[leftIndex] > arr[index]):
            while leftIndex >= 0:
                print(f'arr: {arr} leftIndex: {leftIndex} leftIndexArr: {arr[leftIndex]}')
                # Burada 1.indexde ki sayı 2.indexdeki sayıdan büyük mü diye sordu true aldı  leftIndexi 1 düşürdü ve sayıları yer değiştirdi
                # Left Index 0 oldu ve tekrardan soldaki sayı sağdaki sayıdan büyük mü diye sordu evet alınca soldaki sayıyı sağ yaptı sağdaki sayıyı sol yaptı
                if(arr[leftIndex] > arr[leftIndex + 1]):
                    print(value)
                    arr[leftIndex + 1] = arr[leftIndex]
                    arr[leftIndex] = value
                    leftIndex -= 1
                else:
                    print('çünkü büyük değil')
                    break
    return arr


print(insertionSort2([4,6,1,2]))