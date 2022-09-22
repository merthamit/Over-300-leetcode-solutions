from re import sub


class MyHashSet(object):

    def __init__(self):
        self.arr = [[] for _ in range(1000)]

    def add(self, key):
        subkey = key % 1000
        if not self.contains(key):
            self.arr[subkey].append(key)

    def remove(self, key):
        subkey = key % 1000
        if self.contains(key):
            self.arr[subkey].remove(key)
            
    def contains(self, key):
        subkey = key % 1000
        
        return key in self.arr[subkey]
        

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)

