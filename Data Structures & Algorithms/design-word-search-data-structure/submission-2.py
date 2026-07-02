class WordNode:

    def __init__(self):
        self.children = [None] * 26
        self.endOfWord = False
class WordDictionary:

    def __init__(self):
        self.root = WordNode()

    def addWord(self, word: str) -> None:
        curr = self.root

        for c in word:
            idx = self.get_index(c)
            if not curr.children[idx]:
                curr.children[idx] = WordNode()
            curr = curr.children[idx]
        curr.endOfWord = True

    def search(self, word: str) -> bool:
        return self.dfs(self.root, 0, word)

    def dfs(self, node: WordNode, start_index: int, word: str) -> bool:
        if not node:
            return False
        
        curr = node

        for i in range(start_index, len(word)):
            c = word[i]
            if c == ".":
                for child in curr.children:
                    if self.dfs(child, i+1, word):
                        return True
                return False
            else:
                idx = self.get_index(c)
                if not curr.children[idx]:
                    return False
                curr = curr.children[idx]
        
        return curr.endOfWord

    def get_index(self, ch : int) -> bool:
        return ord(ch) - ord("a")