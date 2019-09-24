def numIslands(self, grid):
    """
    走過的就mark
    """
    if not grid:
        return 0
    def dfs(i,j,gird):
        if i>len(grid)-1 or i<0:
            return 
        if j>len(grid[0])-1 or j<0:
            return
        if grid[i][j]=='1':
            grid[i][j]=0
            dfs(i+1,j,grid)
            dfs(i,j+1,grid)
            dfs(i,j-1,grid)
            dfs(i-1,j,grid)
    count=0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j]=='1':
                dfs(i,j,grid)
                count=count+1
    return count