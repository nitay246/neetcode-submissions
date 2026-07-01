class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        count = 0
        row = len(grid)
        col = len(grid[0])
        for i in range(row):
            for j in range(col):
                if grid[i][j]:
                    if i+1>=row:
                        count += 1
                    else:
                        if not grid[i+1][j]:
                           count += 1 
                    if j+1>=col:
                        count += 1
                    else:
                        if not grid[i][j+1]:
                            count += 1
                    if i-1<0:
                        count += 1
                    else:
                        if not grid[i-1][j]:
                            count += 1
                    if j-1<0:
                        count += 1
                    else:
                        if not grid[i][j-1]:
                            count += 1
                        
        return count

