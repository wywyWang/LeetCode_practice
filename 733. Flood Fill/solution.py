from typing import List

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        '''
        Time: O(m*n), Space: O(1)
        '''
        self.image = image
        self.row, self.col = len(image), len(image[0])
        # edge case
        if self.row == 0 or self.col == 0:
            raise NotImplementedError

        self.visited = set((sr, sc))
        self.old_color = image[sr][sc]
        self.new_color = newColor
        self.image[sr][sc] = newColor
        self.DFS(sr, sc)
        
        return self.image
    
    def DFS(self, sr, sc):
        if (sr, sc) in self.visited:
            return
        else:
            self.visited.add((sr, sc))
        # left
        if sc - 1 >= 0 and self.image[sr][sc-1] == self.old_color:
            self.image[sr][sc-1] = self.new_color
            self.DFS(sr, sc-1)
        # right
        if sc + 1 < self.col and self.image[sr][sc+1] == self.old_color:
            self.image[sr][sc+1] = self.new_color
            self.DFS(sr, sc+1)
        # top
        if sr - 1 >= 0 and self.image[sr-1][sc] == self.old_color:
            self.image[sr-1][sc] = self.new_color
            self.DFS(sr-1, sc)
        # bottom
        if sr + 1 < self.row and self.image[sr+1][sc] == self.old_color:
            self.image[sr+1][sc] = self.new_color
            self.DFS(sr+1, sc)