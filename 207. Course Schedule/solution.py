class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        '''
        Time: O(n); n is the length of prerequisites
        Space: O(n)
        '''
        
        if len(prerequisites) == 0:
            return True
        
        self.graph = [[] for _ in range(numCourses)]
        # create graph
        for pair in prerequisites:
            x, y = pair
            self.graph[x].append(y)
            
        # visit each node
        self.visited = [0 for _ in range(numCourses)]
        for i in range(numCourses):
            if not self.DFS(i):
                return False
        return True
    
    def DFS(self, i):
        # if ith node is marked as being temp visited, then a cycle is found
        if self.visited[i] == -1:
            return False
        # if it is done visted, then do not visit again
        if self.visited[i] == 1:
            return True
        # mark as being temp visited
        self.visited[i] = -1
        # visit all the neighbours
        for neighbor in self.graph[i]:
            if not self.DFS(neighbor):
                return False
        # after visit all the neighbours, mark it as done visited
        self.visited[i] = 1
        return True