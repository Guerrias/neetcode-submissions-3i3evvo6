class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = defaultdict(list)
        visited = set()
        path = [False] * n

        for p1, p2 in edges:
            graph[p1].append(p2)
            graph[p2].append(p1)
        
        def hasCycle(pt: int, parent: int) -> bool:
            if pt in visited:
                return False

            if path[pt]:
                return True
            
            path[pt] = True

            for nei in graph[pt]:
                if nei != parent and hasCycle(nei, pt):
                    return True
            
            visited.add(pt)
            path[pt] = True
        
        if hasCycle(0, -1):
            return False
        
        return len(visited) == n