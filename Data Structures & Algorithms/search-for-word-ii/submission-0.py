class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False
    
    def addWord(self, word: string):
        current = self

        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
        current.endOfWord = True

class Solution:

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        visited, res = set(), set()
        rows, cols = len(board), len(board[0])

        for word in words:
            root.addWord(word)

        def dfs(row, col, node, word):
            if (row < 0 or row == rows or 
                col < 0 or col == cols or
                (row, col) in visited or
                board[row][col] not in node.children):
                return

            visited.add((row, col))
            node = node.children[board[row][col]]
            word += board[row][col]
            if node.endOfWord:
                res.add(word)

            dfs(row + 1, col, node, word)
            dfs(row - 1, col, node, word)
            dfs(row, col + 1, node, word)
            dfs(row, col - 1, node, word)

            visited.remove((row, col))

        
        for row in range(rows):
            for col in range(cols):
                dfs(row, col, root, "")
        
        return list(res)
        

    

