class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        visited = set()
        
        def dfs(board: List[List[str]], word: str, row: int, col:int, pos:int) -> bool:
            #print(row, col, pos)
            if pos == len(word):
                return True
            
            if (row < 0 or row>= rows or
                col < 0 or col>= cols or 
                (row, col) in visited or 
                board[row][col] != word[pos]):
                    return False

            currentCell = (row, col)
            visited.add(currentCell)

            ans = (
                dfs(board, word, row + 1, col, pos+1) or
                dfs(board, word, row - 1, col, pos+1) or
                dfs(board, word, row, col + 1, pos+1) or
                dfs(board, word, row, col - 1, pos+1) )

            visited.remove(currentCell)
            return ans

        for row in range(rows):
            for col in range(cols):
                if dfs(board, word, row, col, 0):
                    return True
        return False
            