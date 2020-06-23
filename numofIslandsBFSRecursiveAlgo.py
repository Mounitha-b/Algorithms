class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count=0
        if grid is None or len(grid) is 0:
            return count
        
        x=len(grid)
        y=len(grid[0])
              
            
        for x1 in range(x):
            for y1 in range(y):
                if(grid[x1][y1]=='1'):
                    self.bfs(grid,x1,y1)
                    count+=1
        return count           
        
    def bfs(self,grid: List[List[str]],x1: int,y1:int):
        if(x1<0 or x1>=len(grid) or y1<0 or y1>=len(grid[0]) or grid[x1][y1]=='0'):
            return
        grid[x1][y1]='0'
        self.bfs(grid,x1-1,y1)
        self.bfs(grid,x1+1,y1)
        self.bfs(grid,x1,y1-1)
        self.bfs(grid,x1,y1+1)
