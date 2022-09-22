# Adamın çözdüğü
# Çözüm sayısı 0 | Hedef 5 çözüm
class MyHashMap(object):

    def __init__(self):
        self.size = 2069
        self.buckets = [[] for _ in range(self.size)]

    def put(self, key, value):
        bucket, i = self.getIdx(key)
        if i < 0:
            bucket.append((key, value))
        else:
            bucket[i] = (key, value)
        
    def get(self, key):
        bucket, i = self.getIdx(key)
        if i < 0:
            return -1
        else:
            return bucket[i][1]
        
    def remove(self, key):
        bucket, i = self.getIdx(key)
        if i < 0:
            return
        else:
            bucket.remove(bucket[i])
        
        
    def getHash(self, key):
        return key % self.size
    
    def getIdx(self, key):
        hashKey = self.getHash(key)
        bucket = self.buckets[hashKey]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                return bucket, i
        
        return bucket, -1
        
            
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)