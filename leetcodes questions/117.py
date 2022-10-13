
# Adamın çözdüğü
# Çözüm sayısı 0 | Hedef 5 çözüm
class Solution(object):
    def connect(self, root):
        if not root: return root
        curr = root
        
        while curr:
            
            dummy = pre = "Node(0)"
            
            while curr:
                
                if curr.left:
                    pre.next = curr.left
                    pre = pre.next
                if curr.right:
                    pre.next = curr.right
                    pre = pre.next
            
                curr = curr.next
            
            curr = dummy.next
            
        return root
            
        
            