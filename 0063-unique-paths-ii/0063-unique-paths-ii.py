class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        # If the start or end cell has an obstacle, zero paths are possible
        if grid[0][0] == 1 or grid[m - 1][n - 1] == 1:
            return 0
        
        # Number of ways to reach the starting cell
        grid[0][0] = 1
        
        # Initialize the first row
        for j in range(1, n):
            grid[0][j] = grid[0][j - 1] if grid[0][j] == 0 else 0
            
        # Initialize the first column
        for i in range(1, m):
            grid[i][0] = grid[i - 1][0] if grid[i][0] == 0 else 0
            
        # Fill the rest of the grid dynamically
        for i in range(1, m):
            for j in range(1, n):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                else:
                    grid[i][j] = grid[i - 1][j] + grid[i][j - 1]
                    
        return grid[m - 1][n - 1]