class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        self.max_d = 0
        self.grid = grid
        self.queue = collections.deque()
        self.row = len(grid)
        self.col = len(grid[0])
        #queue.append(grid[0][0])
        for r in range(self.row):
            for c in range(self.col):
                if grid[r][c] == 2:
                    self.queue.append((r, c, 0))
        while self.queue:
            target = self.queue.popleft()
            print target
            self.BFS(target)
        
        for r in range(self.row):
            for c in range(self.col):
                if self.grid[r][c] == 1:
                    return -1
        return self.max_d
            
            
    def BFS(self, target):
        r = target[0]
        c = target[1]
        d = target[2]
        self.max_d = max(d, self.max_d)
        if r > 0:
            if self.grid[r-1][c] == 1:
                self.grid[r-1][c] = 2
                self.queue.append((r-1, c, d+1))
        if r < self.row - 1:
            if self.grid[r+1][c] == 1:
                self.grid[r+1][c] = 2
                self.queue.append((r+1, c, d+1))
        if c > 0:
            if self.grid[r][c-1] == 1:
                self.grid[r][c-1] = 2
                self.queue.append((r, c-1, d+1))
        if c < self.col - 1:
            if self.grid[r][c+1] == 1:
                self.grid[r][c+1] = 2
                self.queue.append((r, c+1, d+1))
