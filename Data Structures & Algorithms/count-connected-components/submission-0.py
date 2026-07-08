class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        visited = set()

        for p1, p2 in edges:
            graph[p1].append(p2)
            graph[p2].append(p1)

        
        def dfs(node: int) -> None:
            if node in visited:
                return
            
            visited.add(node)
            for nei in graph[node]:
                dfs(nei)


        count = 0
        for i in range(n):
            if i in visited:
                continue
            count += 1
            dfs(i)
        return count
