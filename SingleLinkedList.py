class Node:
    def __init__(self,value=None):
        self.value = value
        self.next = None


class SLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        temp = self.head
        while temp is not None:
            yield temp
            temp = temp.next

    def insertSLL(self, value, location):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            if(location == 0):
                newNode.next = self.head
                self.head = newNode
            elif(location == -1):
                self.tail.next = newNode
                self.tail = newNode
            else:
                temp = self.head
                index = 0
                while index < location - 1:
                    temp = temp.next
                    index += 1
                newNode.next = temp.next
                temp.next = newNode

    def traverseSLL(self):
        if self.head is None:
            return 'No list here.'
        node = self.head
        while node is not None:
            print(node.value)
            node = node.next
        return 'Loop is over.'

    def searchSLL(self,value):
        node = self.head

        while node is not None:
            if(node.value == value):
                return True
            node = node.next
        return False

    def deletionSLL(self, index):
        node = self.head
        counter = 0
        while (index - 1) != counter:
            node = node.next
            counter += 1 
        temp = node.next.next
        node.next = temp

        return self.traverseSLL()
ssLink = SLinkedList()
ssLink.insertSLL('tst',0)
ssLink.insertSLL('something',1)
ssLink.insertSLL('happen',2)
print(ssLink.deletionSLL(1))


a = [1,2,3]
b = a
print(b)