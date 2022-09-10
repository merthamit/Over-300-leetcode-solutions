# Adamın çözdüğü
# Çözüm sayısı 0 | Hedef 5 çözüm
class Solution(object):
    def isValid(self, s):
        stack = []
        closeToOpen = {
            ')' : '(',
            ']' : '[',
            '}' : '{',
        }

        for c in s:
            if c in closeToOpen:
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return True if not stack else False

print(Solution().isValid('[()]'))

