# 44. Trie Implementation and Advanced Operations

class Trie:
    class Node:
        def __init__(self):
            self.child = {}
            self.cp = 0
            self.ew = 0
        def containkey(self, key):
            return key in self.child
        
    def __init__(self):
        self.root = self.Node()

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        temp = self.root
        for w in word:
            if temp.containkey(w):
                temp = temp.child[w]
            else:
                temp.child[w] = self.Node()
                temp = temp.child[w]
            temp.cp += 1
        temp.ew += 1

    def countWordsEqualTo(self, word):
        """
        :type word: str
        :rtype: int
        """
        temp = self.root
        for w in word:
            if not temp.containkey(w):
                return 0
            temp = temp.child[w]
        return temp.ew



    def countWordsStartingWith(self, prefix):
        """
        :type word: str
        :rtype: int
        """
        temp = self.root
        for w in prefix:
            if not temp.containkey(w):
                return 0
            temp = temp.child[w]
        return temp.cp

    def erase(self, word):
        """
        :type word: str
        :rtype: None
        """
        if self.countWordsEqualTo(word) == 0:
            return
        temp = self.root
        for w in word:
            temp = temp.child[w]
            temp.cp -= 1
        temp.ew -= 1

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.countWordsEqualTo(word)
# param_3 = obj.countWordsStartingWith(prefix)
# obj.erase(word)