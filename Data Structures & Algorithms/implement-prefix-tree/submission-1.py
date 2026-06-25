class TrieNode:
    def __init__(self):
        self.children = [None]*26
        self.endOfWord = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        currentNode = self.root
        for ch in word:
            idx = ord(ch) - ord('a')
            if currentNode.children[idx] == None:
                currentNode.children[idx] = TrieNode()
            currentNode = currentNode.children[idx]
        currentNode.endOfWord = True;
                

    def search(self, word: str) -> bool:
        currentNode = self.root
        for ch in word:
            idx = ord(ch) - ord('a')
            if currentNode.children[idx] == None:
                return False
            currentNode = currentNode.children[idx]
        return currentNode.endOfWord;

    def startsWith(self, prefix: str) -> bool:
        currentNode = self.root
        for ch in prefix:
            idx = ord(ch) - ord('a')
            if currentNode.children[idx] == None:
                return False
            currentNode = currentNode.children[idx]
        return True
