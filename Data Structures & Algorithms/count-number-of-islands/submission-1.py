class Solution:
    
    def numIslands(self, grid: List[List[str]]) -> int:
       vis = set()
       n = len(grid)
       m = len(grid[0])
       res = 0
       def bfs(i, j):
        print(i,j,'bfs')
        queue = [(i,j)]
        while queue:
            i,j = queue.pop()
            if (i,j) in vis:
                continue
            vis.add((i,j))
            for i_k, j_k in [(0,1),(1,0),(0,-1), (-1,0)]:
                i_n = i + i_k
                j_n = j + j_k
                if i_n >= 0 and i_n < n and j_n >= 0 and j_n < m and grid[i_n][j_n] == '1':
                    queue.append((i_n,j_n))
    
       for i in range(n):
        for j in range(m):
            entry = grid[i][j]
            if entry == '1' and (i,j) not in vis:
                print('YUUR')
                bfs(i,j) 
                res += 1
        
       return res
    
        
