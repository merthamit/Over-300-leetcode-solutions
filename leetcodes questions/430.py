
# Adamın çözdüğü
# Çözüm sayısı 0 | Hedef 5 çözüm
class Solution(object):
    def flatten(self, head):
        curr = head
        
        while curr:
            if curr.child:
                currNode, tail = self.isChild(curr.child)
                curr.child = None
                nxt = curr.next
                currNode.prev = curr
                if nxt:
                    curr.next.prev = tail
                    tail.next = curr.next
                curr.next = currNode
                    
            curr = curr.next
        return head
      
    def isChild(self, currNode):
        tail = currNode
        while tail.next:
            tail = tail.next
        return [currNode, tail]
            
            
        
        
                
        