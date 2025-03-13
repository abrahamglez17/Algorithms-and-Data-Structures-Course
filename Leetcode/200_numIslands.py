class Solution:
    def dfs(self, grid, i,j): #grid and current location
        #check if in or out of bounds
        if(i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0])):
            return
        
        #if visited leave
        if(grid[i][j]=="0"):
            return
        
        #change to 0 if current cell is 1 and not visited
        grid[i][j]="0" #mark as visited
        
        self.dfs(grid, i+1, j) #down
        self.dfs(grid, i-1, j) #up
        self.dfs(grid, i, j+1) #right
        self.dfs(grid, i, j-1) #left
        
    
    def numIslands(self, grid: list[list[str]]) -> int:
        solution =0
        for i in range(len(grid)): #rows
            for j in range(len(grid[0])): #columns
                if(grid[i][j]=="1"):
                    solution += 1
                    self.dfs(grid, i, j)
        return solution


case1 = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]

case2= [
    ["1","1","0","0","0"],
    ["1","1","0","0","0"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
]

s= Solution()

print(case1)
print(s.numIslands(case1))
print(case2)
print(s.numIslands(case2))