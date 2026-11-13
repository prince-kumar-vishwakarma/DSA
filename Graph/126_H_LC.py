# 126. Word Ladder II


class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: list[str]) -> list[list[str]]:
        wordSet = set(wordList)
        if endWord not in wordSet: return []

        queue = deque([beginWord])
        visited = {beginWord}
        mpp = defaultdict(list)
        found = False
    
        while queue and not found:
            levelVisited = set()
            for _ in range(len(queue)):
                w = queue.popleft()
                wl = list(w)
                for i in range(len(wl)):
                    for j in range(ord('a'), ord('z') + 1):
                        copy = wl[:]
                        copy[i] = chr(j)
                        s = ''.join(copy)
                        if s in wordSet and s != w:
                            if s not in visited:
                                levelVisited.add(s)
                                mpp[s].append(w)
                                if s == endWord: 
                                    found = True
                            elif s in levelVisited:
                                mpp[s].append(w)
            visited.update(levelVisited)
            queue.extend(levelVisited)

        ans = []
        path = [endWord]
        def dfs(word):
            if word == beginWord:
                ans.append(path[::-1])
                return
            for p in mpp[word]:
                path.append(p)
                dfs(p)
                path.pop()
        if found:
            dfs(endWord)
        return ans