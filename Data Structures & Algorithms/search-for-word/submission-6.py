class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        visited = set()

        def dfs(row, col, pos):
            if len(word) == pos:
                return True
            
            curCell = (row, col)

            if (row < 0 or row == rows or
                col < 0 or col == cols or
                curCell in visited or
                board[row][col] != word[pos]):
                return False
            
            visited.add(curCell)

            ans = (
                dfs(row + 1, col, pos +1) or
                dfs(row - 1, col, pos +1) or
                dfs(row, col +1, pos +1) or
                dfs(row, col -1, pos +1)
            )

            visited.remove(curCell)
            return ans

        for row in range(rows):
            for col in range(cols):
                if dfs(row, col, 0):
                    return True
        return False