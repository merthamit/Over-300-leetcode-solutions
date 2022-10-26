# Adamın çözdüğü
# Çözüm sayısı 0 | Hedef 5 çözüm
class Solution(object):
    def isSameTree(self, p, q):
        if not p and not q: return True
        if not p or not q: return False
        if p.val != q.val: return False
        
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

# Adamın çözdüğü
# Çözüm sayısı 0 | Hedef 5 çözüm
class Solution(object):
    def isSameTree(self, p, q):
        stack = [(p, q)]
        while len(stack):
            first, second = stack.pop()
            if not first and not second: pass
            elif not first or not second: return False
            else:
                if first.val != second.val: return False
                stack.append((first.left, second.left))
                stack.append((first.right, second.right))
        
        return True