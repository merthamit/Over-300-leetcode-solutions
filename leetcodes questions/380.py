from random import random


class RandomizedSet(object):

    def __init__(self):
        self.arr = []
        self.dictArr = {}

    def insert(self, val):
        if not val in self.dictArr:
            self.dictArr[val] = len(self.arr)
            self.arr.append(val)
            return True
        return False        
    def remove(self, val):
        if val in self.dictArr:
            self.dictArr[self.arr[-1]] = self.dictArr[val]
            self.arr[self.dictArr[val]] = self.arr[-1]
            
            self.arr.pop()
            self.dictArr.pop(val)
            return True
        return False
        

    def getRandom(self):
        return random.choice(self.arr)

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
