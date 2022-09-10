class Node:
    def __init__(self,data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beggining(self,data):
        node = Node(data)
        if(self.head != None):
            node = Node(data, self.head)
        self.head = node

    def print(self):
        if self.head == None:
            print('Linked list empty...')
            return
        
        itr = self.head
        llstr = ''
        while itr:
            llstr += f'{itr.data} --> '
            itr = itr.next
        print(llstr)

    def insert_at_end(self,data):
        node = Node(data)
        if(self.head == None):
            self.head = node
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = node

    def insert_values(self,datalist):
        self.head = None
        for data in datalist:
            self.insert_at_end(data)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            itr = itr.next
            count +=1
        return count

    def remove_at(self, index):
        if((index < 0) or (index > self.get_length() - 1) or self.get_length() == 0):
             raise Exception('Index cannot be negative or more than length')
        itr = self.head
        
        if(index == 0):
            self.head = self.head.next
            return 
        
        while index-1:
            itr = itr.next     
            index -= 1
        itr.next = itr.next.next

    def insert_at(self,index,data):
        if((index < 0) or (index > self.get_length())):
             raise Exception('Index cannot be negative or more than length')
        itr = self.head
        if(index == 0):
            self.insert_at_beggining(data)
            return
        while index - 1:
            itr = itr.next
            index -=1
        itr.next = Node(data, itr.next)

a = LinkedList()
a.insert_values([1,2,3,4,5,6,7])
a.insert_at(0,31)
a.print()