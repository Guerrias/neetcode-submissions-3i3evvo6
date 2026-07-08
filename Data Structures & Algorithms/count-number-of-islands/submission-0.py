class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        directions = [[0,1], [0,-1], [-1,0], [1,0]]
        def dfs(row, col) -> None:
            if ( min(row, col) < 0 or
                row >= len(grid) or col >= len(grid[0]) or
                grid[row][col] != "1" or (row, col) in visited) :
                return
            
            visited.add((row, col))

            for direction in directions:
                newRow = row + direction[0]
                newCol = col + direction[1]

                dfs(newRow, newCol)
        
        count = 0
        for row in range(len(grid)) :
            for col in range(len(grid[0])):
                if grid[row][col] == "1" and (row, col) not in visited:
                    count += 1
                    dfs(row, col)
        return count