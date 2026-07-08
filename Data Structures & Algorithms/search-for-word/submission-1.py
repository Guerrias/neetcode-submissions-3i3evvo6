class Solution:
    def __init__(self):
        self.rows = 0
        self.cols = 0
        self.directions = [[0, 1], [0, -1], [-1, 0], [1, 0]]
        self.visited = set()

    def exist(self, board: List[List[str]], word: str) -> bool:
        self.rows = len(board)
        self.cols = len(board[0])
        for row in range(self.rows):
            for col in range(self.cols):
                #if board[row][col] == word[0]:
                if self.dfs(board, word, row, col, 0):
                    return True
        return False

    def dfs(self, board: List[List[str]], word: str, row: int, col:int, pos:int) -> bool:
        #print(row, col, pos)
        if pos == len(word):
            return True
        
        if (row < 0 or row>= self.rows or
            col < 0 or col>= self.cols or 
            (row, col) in self.visited or 
            board[row][col] != word[pos]):
                return False

        currentCell = (row, col)
        self.visited.add(currentCell)

        for direction in self.directions:
            newRow = row + direction[0]
            newCol = col + direction[1]

            if self.dfs(board, word, newRow, newCol, pos+1):
                return True

        self.visited.remove(currentCell)
        return False
            