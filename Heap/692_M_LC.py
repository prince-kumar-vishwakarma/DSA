# 692. Top K Frequent Words
# https://leetcode.com/problems/top-k-frequent-words/description/

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        hm = {}
        for word in words:
            hm[word] = hm.get(word, 0) + 1
        heap = []
        for key, value in hm.items():
            heapq.heappush(heap, (-value, key))

        return [heapq.heappop(heap)[1] for _ in range(k)]
        