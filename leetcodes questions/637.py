import collections

# Adamın çözdüğü
# Çözüm sayısı 0 | Hedef 5 çözüm
class Solution(object):
    def averageOfLevels(self, root):
        res = []
        q = collections.deque()
        q.append(root)

        while q:
            total = 0
            lng = len(q)

            for _ in range(lng):
                node = q.popleft()
                total += node.val

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            res.append(float(total) / lng)
        
        return res
        