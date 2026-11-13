# 208. Implement Trie (Prefix Tree)

class Trie:
    class TrieNode:
        def __init__(self):
            self.children = {}
            self.end = False
        
        def containKey(self, c:str) -> bool:
            return c in self.children
        
        def setEnd(self) -> None:
            self.end = True

    def __init__(self):
        self.root = self.TrieNode()

    def insert(self, word: str) -> None:
        temp = self.root
        for w in word:
            if temp.containKey(w): 
                temp = temp.children[w]
            else:
                temp.children[w] = self.TrieNode()
                temp = temp.children[w]
        temp.setEnd()
        

    def search(self, word: str) -> bool:
        temp = self.root
        for w in word:
            if not temp.containKey(w):
                return False
            temp = temp.children[w]
        
        return temp.end
        

    def startsWith(self, prefix: str) -> bool:
        temp = self.root
        for w in prefix:
            if not temp.containKey(w):
                return False
            temp = temp.children[w]
        
        return True
        

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)