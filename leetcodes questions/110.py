# Adamın çözdüğü
# Çözüm sayısı 0 | Hedef 5 çözüm
class Solution(object):
    def isBalanced(self, root):
        if not root: return True
        if not root.left and not root.right: return True
        
        def dfs(root):
            if not root: return [True, 0]

            left = dfs(root.left)
            right = dfs(root.right)
            balanced = (left[0] and right[0] and abs(right[1] - left[1]) <= 1)            
            
            return [balanced, max(left[1], right[1]) + 1]
        
        
        return dfs(root)[0]
        
# Burada olay şu normalde abs() kısmını döndersek yetiyor fakat derinliği döndermemiş oluyoruz o yüzden iksini böyle dönderiyoruz.