from collections import deque
import collections
# Adamın çözdüğü
# Çözüm sayısı 0 | Hedef 5 çözüm
class Solution(object):
    def openLock(self, deadends, target):
        if '0000' in deadends: return -1
        q = collections.deque()
        visit = set(deadends)

        def children(num):
            ch = []
            for i in range(4):
                digit = str((int(num[i]) + 10 + 1) % 10)
                ch.append(num[:i] + digit + num[i+1:])
                digit = str((int(num[i]) + 10 - 1) % 10)
                ch.append(num[:i] + digit + num[i+1:])
            return ch

        q.append(('0000', 0))

        while q:
            num, turn = q.popleft()
            if num == target: return turn
            for child in children(num):
                if child not in visit:
                    visit.add(child)
                    q.append((child, turn + 1))
        
        return -1


print(Solution().openLock(["0201","0101","0102","1212","2002"], "0202"))
