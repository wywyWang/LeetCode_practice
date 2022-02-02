from typing import List

'''
first add 4, reach next will minus 1 and next will add 3
'''

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        '''
        Time: O(V+E), space: O(1)
        '''
        self.grid = grid
        ans = 0

        # edge case
        self.row = len(grid)
        if self.row == 0:
            return ans
        else:
            self.col = len(grid[0])
            if self.col == 0:
                return ans

        for rid in range(self.row):
            for cid in range(self.col):
                if grid[rid][cid] == 1:
                    ans += 4
                    grid[rid][cid] = 2          # 2 means visited land
                    ans = self.DFS(rid, cid, ans)
                    return ans                  # only one island, no need to run all

        return ans

    def count_visited(self, rid: int, cid: int) -> int:
        visited_neighbors = 0
        # left
        if cid - 1 >= 0 and self.grid[rid][cid-1] == 2:
            visited_neighbors += 1
        # right
        if cid + 1 < self.col and self.grid[rid][cid+1] == 2:
            visited_neighbors += 1
        # top
        if rid - 1 >= 0 and self.grid[rid-1][cid] == 2:
            visited_neighbors += 1
        # bottom
        if rid + 1 < self.row and self.grid[rid+1][cid] == 2:
            visited_neighbors += 1
        return visited_neighbors

    def DFS(self, rid: int, cid: int, ans: int) -> int:
        # left
        if cid - 1 >= 0 and self.grid[rid][cid-1] == 1:
            ans += 4
            ans -= 2 * self.count_visited(rid, cid-1)
            self.grid[rid][cid-1] = 2
            ans = self.DFS(rid, cid-1, ans)
        # right
        if cid + 1 < self.col and self.grid[rid][cid+1] == 1:
            ans += 4
            ans -= 2 * self.count_visited(rid, cid+1)
            self.grid[rid][cid+1] = 2
            ans = self.DFS(rid, cid+1, ans)
        # top
        if rid - 1 >= 0 and self.grid[rid-1][cid] == 1:
            ans += 4
            ans -= 2 * self.count_visited(rid-1, cid)
            self.grid[rid-1][cid] = 2
            ans = self.DFS(rid-1, cid, ans)
        # bottom
        if rid + 1 < self.row and self.grid[rid+1][cid] == 1:
            ans += 4
            ans -= 2 * self.count_visited(rid+1, cid)
            self.grid[rid+1][cid] = 2
            ans = self.DFS(rid+1, cid, ans)

    return ans