from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ans = 0

        # edge case
        if grid is None:
            return ans
        else:
            n_row = len(grid)

        # edge case
        if n_row == 0:
            return ans
        else:
            n_col = len(grid[0])
        
        # edge case
        if n_col == 0:
            return ans

        def DFS(row, col):
            # left
            if col - 1 >= 0:
                if grid[row][col-1] == "1":
                    grid[row][col-1] = "0"
                    DFS(row, col-1)
            # right
            if col + 1 < n_col:
                if grid[row][col+1] == "1":
                    grid[row][col+1] = "0"
                    DFS(row, col+1)
            # down
            if row + 1 < n_row:
                if grid[row+1][col] == "1":
                    grid[row+1][col] = "0"
                    DFS(row+1, col)
            # up
            if row - 1 >= 0:
                if grid[row-1][col] == "1":
                    grid[row-1][col] = "0"
                    DFS(row-1, col)

        for row in range(n_row):
            for col in range(n_col):
                if grid[row][col] == "1":
                    grid[row][col] == "0"
                    ans += 1
                    DFS(row, col)

        return ans
    

solution = Solution()

# test data 1
grid = [
    ["1","1","1","1","0"],
    ["1","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","0","0","0","0"]
]
print(solution.numIslands(grid))

# test data 2
grid = [
    ["1","1","0","0","0"],
    ["1","1","0","0","0"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
]
print(solution.numIslands(grid))

# test data 3
grid = None
print(solution.numIslands(grid))

# test data 4
grid = []
print(solution.numIslands(grid))

# private test data 1
grid = [
    ["1","1","1"], 
    ["0","1","0"], 
    ["1","1","1"]
]
print(solution.numIslands(grid))