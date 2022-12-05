class StockSpanner(object):

    def __init__(self):
        self.stack = []

    def next(self, price):
        span = 1
        while self.stack and self.stack[-1][0] <= price:
            lastSpan = self.stack.pop()[1]
            span += lastSpan
            
        self.stack.append((price, span))
        return span     
            
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)