from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        def DFS(row, col):
            if grid[row][col] == '1':
                grid[row][col] = '0'
                if row - 1 >= 0 and grid[row-1][col] == '1':
                    DFS(row-1, col)        # up
                if row + 1 < max_row and grid[row+1][col] == '1':
                    DFS(row+1, col)        # down
                if col - 1 >= 0 and grid[row][col-1] == '1':
                    DFS(row, col-1)        # left
                if col + 1 < max_col and grid[row][col+1] == '1':
                    DFS(row, col+1)        # right
        
        ans = 0
        max_row, max_col = len(grid), len(grid[0])
        for row in range(max_row):
            for col in range(max_col):
                if grid[row][col] == '1':
                    ans += 1
                    DFS(row, col)
        
        return ans