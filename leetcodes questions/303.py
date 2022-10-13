class NumArray(object):

    def __init__(self, nums):
        self.accu = [0]
        for num in nums:
            self.accu.append(num + self.accu[-1])

    def sumRange(self, left, right):
        return self.accu[right+1] - self.accu[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)