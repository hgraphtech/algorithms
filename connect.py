n = int(input())
r,c=map(int,input().split())
s=(r-1,c-1)
r,c=map(int,input().split())
e=(r-1,c-1)
grid = []
for n_ in range(n):
    z=input()
    grid.append([int(z[i]) for i in range(n)])

g = []
g.append(s)
found = False

while len(g)>0:
    x,y = g[0]
    
    if (x,y)==e:
        print(0)
        found = True
        break
    
    grid[x][y]=2

    if x>0:
        if grid[x-1][y]==0:
            grid[x-1][y]=2
            g.append((x-1,y))
    if y>0:
        if grid[x][y-1]==0:
            grid[x][y-1]=2
            g.append((x,y-1))
    if x<n-1:
        if grid[x+1][y]==0:
            grid[x+1][y]=2
            g.append((x+1,y))
    if y<n-1:
        if grid[x][y+1]==0:
            grid[x][y+1]=2
            g.append((x,y+1))
    
    g.remove(g[0])

if found == False:

    x,y = e
    nearest = 100000

    g = []
    g.append(e)

    while len(g)>0:
        x,y = g[0]
        grid[x][y]=3

        for x_ in range(n):
            for y_ in range(n):
                if grid[x_][y_] == 2:

                    dist = (x-x_)**2 + (y-y_)**2

                    if dist<nearest:
                        nearest=dist


        if x>0:
            if grid[x-1][y]==0:
                g.append((x-1,y))
        if y>0:
            if grid[x][y-1]==0:
                g.append((x,y-1))
        if x<n-1:
            if grid[x+1][y]==0:
                g.append((x+1,y))
        if y<n-1:
            if grid[x][y+1]==0:
                g.append((x,y+1))

        g.remove(g[0])

    print(nearest)