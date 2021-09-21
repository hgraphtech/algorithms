
t = int(input())
for t_ in range(t):

    xa,ya,xb,yb = map(int,input().split())
    x = xb-xa
    y = yb-ya
    
    print(x*y+1)
