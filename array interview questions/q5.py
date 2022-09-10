myList = [1,2,3,4,5,6]

def isUnique(arr):
    hash = {}
    for idx, i in enumerate(arr):
        if(hash.get(i)):
            return False
        hash[i] = 1
    print(hash)
    return True


print(isUnique(myList))




# def isUnique(arr):
#     hash = {}
#     for idx, i in enumerate(arr):
#         try:
#             hash[i] = hash[i] + idx
#             return False
#         except:
#             return True
# @@@@@ Bu fonksiyon True dönderiyor çünkü try da denediği şey error veriyor bir alt satıra bakmadan excepte gidiyor...