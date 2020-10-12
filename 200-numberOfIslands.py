class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        
        #initial visited states
        self.v = []
        ans = 0
        for i in range(len(grid)):
            self.v.append([])
            for j in range(len(grid[i])):
                self.v[i].append(0)
                
        #self.v[0].append(grid[0][0])
        for x in range(len(grid)):
            for y in range(len(grid[x])):
                if self.v[x][y] == 0 and grid[x][y] == '1':
                    ans += 1
                    self.dfs(grid, x, y)
        return ans
                
    def dfs(self, grid, x, y):
        self.v[x][y] = 1
        if x -1 >= 0 and self.v[x-1][y] == 0 and grid[x-1][y] == '1':
            self.dfs(grid, x -1, y)
        if x + 1 < len(grid) and self.v[x+1][y] == 0 and grid[x+1][y] == '1':
            self.dfs(grid, x+1, y)
        if y -1 >= 0 and self.v[x][y-1] == 0 and grid[x][y-1] == '1':
            self.dfs(grid, x, y-1)
        if y + 1 < len(grid[x]) and self.v[x][y+1] == 0 and grid[x][y+1] == '1':
            self.dfs(grid, x, y+1)
                
                
