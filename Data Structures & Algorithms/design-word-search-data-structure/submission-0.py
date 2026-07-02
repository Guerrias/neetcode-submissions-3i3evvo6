class WordNode:
    def __init__(self):
        self.children = [None] * 26
        self.endOfWord = False
 
class WordDictionary:

    def __init__(self):
        self.root = WordNode()        

    def addWord(self, word: str) -> None:
        current = self.root
        for ch in word :
            i = self.get_index(ch)
            if not current.children[i] :
                current.children[i] = WordNode()
            current = current.children[i]
        current.endOfWord = True 

    def search(self, word: str) -> bool:
        return self.dfs(self.root, 0, word)

    def dfs(self, node: WordNode, start_idx: int, word: str) -> bool:
        if not node:
            return False
    
        curr = node
        for i in range(start_idx, len(word)) :
            c = word[i]
            if c == "." :
                for child in curr.children :
                    if self.dfs(child, i+1, word) :
                        return True
                return False
            else :
                idx = self.get_index(c)
                if not curr.children[idx]:
                    return False
                curr = curr.children[idx]
        return curr.endOfWord

    def get_index(self, char : int) -> int :
        return ord(char) - ord('a')