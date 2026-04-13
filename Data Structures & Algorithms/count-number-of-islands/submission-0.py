class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = []
        queue = []
        res = 0

        for j in range(len(grid)):
            for i in range(len(grid[j])):
                if grid[j][i] == '1' and (j,i) not in visited:
                    res+= 1
                    queue.append((j,i))
                    while len(queue):
                        print(f'visited: {visited}')
                        jc,ic = queue.pop(0)
                        visited.append((jc,ic))
                        if jc - 1 >= 0 and (jc-1,ic) not in visited and (jc-1,ic) not in queue and '1' == grid[jc-1][ic]:
                            queue.append((jc-1,ic))
                        if jc +1 < len(grid) and (jc + 1, ic) not in visited and (jc+1,ic) not in queue and '1' == grid[jc+1][ic]:
                            queue.append((jc+1,ic))
                        if ic - 1 >= 0 and (jc,ic - 1) not in visited and (jc,ic - 1) not in queue and '1' == grid[jc][ic-1]:
                            queue.append((jc, ic -1))
                        if ic +1 < len(grid[j]) and (jc,ic + 1) not in visited and (jc,ic + 1) not in queue and '1' == grid[jc][ic+1]:
                            queue.append((jc, ic + 1))
                else:
                    visited.append((j,i))
        return res