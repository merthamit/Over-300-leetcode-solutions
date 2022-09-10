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

    def createList(self,value):
        node = Node(value)
        self.head = node
        node.next = node
        self.tail = node
    
    def insertList(self,location,value):
        if self.head is None:
            return False
        else:
            newNode = Node(value)
            if location == 0:
                newNode.next = self.head
                self.head = newNode
                self.tail.next = newNode
            elif location == 1:
                newNode.next = self.tail.next
                self.tail.next = newNode
                self.tail = newNode
            else:
                temp = self.head
                index = 0

                while index < location -1:
                    tempNode = temp.next
                    index +=1

                nextNode = tempNode.next
                newNode.next = nextNode
                tempNode.next = newNode

    def traversal(self):
        node = self.head
        while True:
            print(node.value)
            node = node.next
            if(self.tail.next == node):
                break                



newList = SLinkedList()
newList.createList('a')
newList.insertList(1,'test')
newList.insertList(2,'here')
newList.insertList(2,'ehehehe')
newList.insertList(0,'begegedehehehe')
newList.traversal()


print(newList.head.next.next.next.next.value)