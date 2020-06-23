class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count=0
        if grid is None or len(grid)==0:
            return count
        m=len(grid)
        n=len(grid[0])
        
        
        def bfs(i: int,j:int):
            q=collections.deque() #doubly ended que
            q.append((i,j))
            grid[i][j]='0'
            direction=[(0,1),(0,-1),(1,0),(-1,0)]
            
            while q:
                r,c =q.popleft()
                for d in direction:
                    r1=r+d[0]
                    c1=c+d[1]
                    if(r1>=0 and c1 >=0 and r1<m and c1<n and grid[r1][c1]=='1'):
                        q.append((r1,c1))
                        grid[r1][c1]='0'    
        
        for i in range(m):
            for j in range(n):

                if(grid[i][j]=='1'):
 
                    count+=1
                    bfs(i,j)
        return count             
        
    
