# Adamın çözdüğü
# Çözüm sayısı 0 | Hedef 5 çözüm
class Solution(object):
    def backspaceCompare(self, s, t):
        return self.backClean(s) == self.backClean(t)

    def backClean(self, strs):
        stack = []
        for c in strs:
            if c == '#':
                if stack: stack.pop()
            else:
                stack.append(c)
        return stack

print(Solution().backspaceCompare("y#fo##f","y#f#o##f"))

