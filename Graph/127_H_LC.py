# 127. Word Ladder

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        wordSet = set(wordList)
        if endWord not in wordSet: return 0
        ans = 1
        queue = deque([beginWord])
        visited = {beginWord}
        while queue:
            n = len(queue)
            for _ in range(n):
                wl = list(queue.popleft())
                for i in range(len(wl)):
                    for j in range(ord('a'), ord('z') + 1):
                        copy = wl[:]
                        copy[i] = chr(j)
                        s = ''.join(copy)
                        if s in wordSet and s not in visited:
                            if s == endWord:
                                return ans + 1
                            visited.add(s)
                            queue.append(s)
            ans += 1
        return 0