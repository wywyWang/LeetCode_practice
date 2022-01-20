from typing import List


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        ans = 0
        m = len(grid)
        # edge case
        if m == 0:
            return ans
        else:
            n = len(grid[0])
            
        row, col = m - 1, 0
        
        while row >= 0 and col < n:
            if grid[row][col] < 0:
                ans += (n - col)
                row -= 1
            else:
                col += 1
            
        return ans


grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
solution = Solution()
ans = solution.countNegatives(grid)
print(ans)