class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        frut = []
        dirs = [(0,1),(1,0),(0,-1),(-1,0)]
        n = len(grid)
        m = len(grid[0])
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    frut.append((i,j))
        res = 0
        queue = frut
        while queue:
            new_queue = []
            print(queue,res)
            for i,j in queue:
                for nc,nr in dirs:
                    ni, nj = i + nc, j + nr
                    if ni >= 0 and nj >= 0 and ni < n and nj < m and grid[ni][nj] == 1:
                        new_queue.append((ni,nj))
                        grid[ni][nj] = 2
            if new_queue:
                res += 1
            queue = new_queue 
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    return -1
        return res

        