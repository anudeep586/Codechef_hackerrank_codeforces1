grid=[[1,3,1],[1,5,1],[4,2,1]]
if len(grid) <= 0 or grid is None:
    print(0)
rows = len(grid)
cols = len(grid[0])
for r in range(rows):
    for c in range(cols):
        if r==0 and c==0:
            continue
        if r-1<0: 
            grid[r][c] = grid[r][c] + grid[r][c-1]
        elif c-1<0: 
            grid[r][c] = grid[r][c] + grid[r-1][c]  
        else:
            grid[r][c] = grid[r][c] + min(grid[r-1][c], grid[r][c-1])               

print(grid[rows-1][cols-1])
