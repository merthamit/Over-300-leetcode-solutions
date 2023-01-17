class Node(object):
    def __init__(self, url):
        self.url = url
        self.next = None 
        self.prev = None
    
class BrowserHistory(object):

    def __init__(self, homepage):
        self.head = Node(homepage)
        
    def visit(self, url):
        newURL = Node(url)
        newURL.prev = self.head
        self.head.next = newURL
        self.head = self.head.next

    def back(self, steps):
        while steps and self.head.prev:
            self.head = self.head.prev
            steps -= 1
        return self.head.url
        
    def forward(self, steps):
        while steps and self.head.next:
            self.head = self.head.next
            steps -= 1
        return self.head.url

class BrowserHistory:    
    def __init__(self, homepage):
        self.i = 0
        self.len = 1
        self.history = [homepage]

    # O(1)
    def visit(self, url):
        if len(self.history) < self.i + 2:
            self.history.append(url)
        else:
            self.history[self.i + 1] = url
        self.i += 1
        self.len = self.i + 1

    # O(1)
    def back(self, steps):
        self.i = max(self.i - steps, 0)
        return self.history[self.i]

    # O(1)
    def forward(self, steps):
        self.i = min(self.i + steps, self.len - 1)
        return self.history[self.i]

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)