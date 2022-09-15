from collections import Counter
import heapq


# Adamın çözdüğü
# Çözüm sayısı 0 | Hedef 5 çözüm
class Solution(object):
    def topKFrequent(self, words, k):
        count = Counter(words)
        
        heap = [(-freq, word) for word, freq in count.items()]
        heapq.heapify(heap)

        return [heapq.heappop(heap)[1] for _ in range(k)]


print(Solution().topKFrequent(["i","love","leetcode","i","love","coding"], 2))
# print(Solution().topKFrequent(["a","aa","aaa"], 1))
# print(Solution().topKFrequent(["aaa","aa","a"], 1))
