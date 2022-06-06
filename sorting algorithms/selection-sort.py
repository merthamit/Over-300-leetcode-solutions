# Best case o(n^2)
# Average case o(n^2)
# Worst case o(n^2)

#Bu ilk yaptığım kendi düşüncemle bu da O(n^2) fakat içeride 3 tane constant var ve çok çok az da olsa performans kaybı olabilir.
def selectionSort(arr):
    for i in range(0, len(arr)):
        for j in range(i+1, len(arr)):
            print(j)
            if(arr[i] > arr[j]):
                tmp = arr[i]
                arr[i] = arr[j]                
                arr[j] = tmp
    return arr


def selectionSort2(arr):
    # Neden len arr -1 dedim çünkü sondan bir önceki indexe geldiğinde 1 tane rakam kalıyor geriye onuda j kontrol edip yer değiştirecek yada
    # değiştirmeyecek eğer son indexede giderse eğer j nin bir sonraki rakamı olmayacak ve hata vermez ama boş yere range ile boş bir değer oluşturacak.
    # list(range(6,6)) --> boş bir liste dönderecektir.
    for i in range(0, len(arr)-1):
        print(arr, i)
        min = i
        for j in range(i+1, len(arr)):
            # print(j)
            # burada yer değiştirme olmuyor sadece fake bir şekilde indexini tutuyoruz döngü bittikten sonra yer değiştirme gerçekleşiyor...
            if(arr[min] > arr[j]):
                min = j
        tmp = arr[i]
        arr[i] = arr[min]   
        arr[min] = tmp
    return arr


print(selectionSort2([5,4,1,2,0,-1]))
