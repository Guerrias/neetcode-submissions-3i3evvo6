class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        visited = [False] * numCourses
        completed = [False] * numCourses

        for edge1, edge2 in prerequisites:
            graph[edge1].append(edge2)
            graph[edge2]
        
        #print(graph)

        def hasCycle(num: int) -> bool:
            if completed[num]:
                return False
            
            if visited[num]:
                return True
        
            visited[num] = True
            
            for nei in graph[num]:
                if hasCycle(nei):
                    return True
            
            visited[num] = False
            completed[num] = True
            return False
                
        for num in range(numCourses):
            if hasCycle(num):
                return False
        
        return True